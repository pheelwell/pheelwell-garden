import os
import json
import frontmatter
import markdown
import openai
import argparse
# example usage:
# python generate_embeddings.py --path promised-victory --embeddings embeddings_v6.json --mode files --max_length 2000 

# argparse
parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default='promised-victory', help='path to the folder with the markdown files')
parser.add_argument('--embeddings', type=str, default='embeddings.json', help='path to embeddings file')
parser.add_argument('--mode', type=str, default='files', help='files or paragraphs')
parser.add_argument('--max_length', type=int, default=5000, help='max length of one embedding')
args = parser.parse_args()



# API KEY
openai.api_key = "<your api key>"

# embeddings file
embeddings_file = args.embeddings
# the file holds the embeddings and a path to file + line number
''' example embeddings file:
[
    {
        "embeddings": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10],
        "path": "promised-victory/Landing Page.md",
        "from_line": 1,
        "to_line": 3
    },
    {
        "embeddings": [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.10],
        "path": "promised-victory/Landing Page.md",
        "from_line": 4,
        "to_line": 6
    }
    ...

'''
## for now just use one file
##fileURL = 'promised-victory/Landing Page.md'
##files = [fileURL]

# ignored files
ignored_folder = ['.obsidian', '.DS_Store','resources','.git','wedding', 'Technical']
fileending = '.md'

# get all files in the directory exlude .obsidian
files = []
for r, d, f in os.walk(args.path):
    for file in f:
        if file.endswith(fileending) and not any(x in r for x in ignored_folder):
            files.append(os.path.join(r, file))

# for progress bar
total = len(files)
print (f'found {total} files')
print (files)

embeddings_data = []

# loop through all files
for fileURL in files:
    print (f'({files.index(fileURL)}/{total}) processing {os.path.basename(fileURL)} ')
    post = frontmatter.load(fileURL)
    # seperate the note by headdings (group paragraphs together)

    if args.mode == 'headings':
        md = markdown.Markdown()
        content= [] # array of dicts
        # remember the linenumber to be able to find the original text
        # example segment:
        # {
        #     "path": "promised-victory/Landing Page.md",
        #     "from_line": 1,
        #     "to_line": 3
        #     "content": "Content in the segment\n over multiple lines"
        #  }
        # use enumerate to get the line number
        for i, line in enumerate(md.convert(post.content).split('\n')):
            # check if the line is a heading or first line of the file
            if line.startswith('<h') or i == 0:
                # if it's a heading, add the segment to the content array
                # for the first line include the frontmatter
                line = frontmatter.dumps(post) + line
                # also add filename (get from fileURL basename)
                line = f'\n\n# {os.path.basename(fileURL)}\n\n' + line
                content.append({
                    "path": fileURL,
                    "from_line": i,
                    "to_line": i,
                    "content": line
                })
            else:
                # if it's not a heading, append the line to the last segment
                content[-1]['content'] += line
                content[-1]['to_line'] = i

        # remove the first segment (it's empty)
        content = content[1:]

        # now we have a list of segments, we can use gpt to generate embeddings for each segment
        for i, line in enumerate(content):

            # we use the embedding api to generate embeddings for each segment
            response = openai.Embedding.create(
                input=line['content'],
                model="text-embedding-ada-002"
            )
            embeddings = response['data'][0]['embedding']
            # add the new embedding
            embeddings_data.append({
                "embeddings": embeddings,
                "path": fileURL,
                "from_line": line['from_line'],
                "to_line": line['to_line']
            })
            
            # progress bar
            print(f'{i+1}/{len(content)}', end='\r')
    elif args.mode == 'files':
        # dont add if below 100 characters
        if len(post.content) < 100:
            print (f'({files.index(fileURL)}/{total}) skipping {os.path.basename(fileURL)} because it\'s too short')
            continue

        segments = []
        if len(post.content) < args.max_length:
            segments.append(post.content)
        else:
            # split into segments
            # split by line
            lines = post.content.split('\n')
            # split by line length
            line_length = 0
            segment = ''
            for line in lines:
                if line_length + len(line) < args.max_length:
                    segment += line + '\n'
                    line_length += len(line)
                else:
                    segments.append(segment)
                    segment = line + '\n'
                    line_length = len(line)
            # add last segment
            segments.append(segment)
        
        # now we have a list of segments, we can use gpt to generate embeddings for each segment
        for i, segment in enumerate(segments):
            # generate embeddings
            response = openai.Embedding.create(
                input=post.content,
                model="text-embedding-ada-002"
            )
            embeddings = response['data'][0]['embedding']
            
            # copy metadata and add empty content
            metadata = post.metadata
            metadata['content'] = ''
            # add the new embedding
            embeddings_data.append({
                "embeddings": embeddings,
                "path": fileURL,
                "from_line": 1,
                "to_line": len(post.content.split('\n')),
                "metadata": metadata
            })
            
            # progress bar
            print(f'{i+1}/{len(segments)}', end='\r')


# remove if alreasdy exists
if os.path.exists(embeddings_file):
    os.remove(embeddings_file)
# write embeddings file back to disk (could have umlaute in the content, so encode as utf-8)
with open(embeddings_file, 'w', encoding = 'utf-8') as f:
    json.dump(embeddings_data, f)
