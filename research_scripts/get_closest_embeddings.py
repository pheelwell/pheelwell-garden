# this scripts looks at the embeddings.json and finds the closests embeddings until it has loaded the given number of characters

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

# example usage: 
# python get_closest_embeddings.py --embeddings embeddings.json --num_chars 10000 --input_text "this is a test"
# will load 10000 characters

import json
import argparse
import numpy as np
import frontmatter
import markdown
import openai
import os
import markdownify
# argparse
parser = argparse.ArgumentParser()
parser.add_argument('--embeddings', type=str, default='embeddings.json', help='path to embeddings file')
parser.add_argument('--num_chars', type=int, default=10000, help='number of characters to load')
parser.add_argument('--input_text', type=str, default='', help='input text that should be used to find the closest embeddings')
args = parser.parse_args()

# load embeddings
with open(args.embeddings, 'r') as f:
    embeddings = json.load(f)

# API KEY
openai.api_key = "<your api key>"

# generate embeddings for input text
response = openai.Embedding.create(
    input=args.input_text,
    model="text-embedding-ada-002"
)
embedding = response['data'][0]['embedding']

# find closest embeddings and append the path and line number to the list
closest_embeddings = []
for i, e in enumerate(embeddings):
    # calculate the distance
    distance = np.linalg.norm(np.array(embedding) - np.array(e['embeddings']))
    # append the path and line number
    closest_embeddings.append({
        'path': e['path'],
        'from_line': e['from_line'],
        'to_line': e['to_line'],
        'distance': distance
    })

# sort the list by distance
closest_embeddings = sorted(closest_embeddings, key=lambda k: k['distance'])


# load the files and print the text until the given number of characters is reached
# first group by files
loaded = {}
num_chars = 0
for i, e in enumerate(closest_embeddings):
    print(f'loading {e["path"]} from line {e["from_line"]} to line {e["to_line"]}')
    # load the file as unicode
    post = frontmatter.load(e['path'])
    # seperate the note by headdings (group paragraphs together)
    md = markdown.Markdown()
    content= []
    # get the text from the from_line and to_line 
    for i, line in enumerate(md.convert(post.content).split('\n')):
        if i >= e['from_line'] and i <= e['to_line']:
            content.append(line)
    # join the paragraphs together (adding a linebreak)
    content = '\n'.join(content)
    # add the text to the loaded text
    loaded[e['path']] = loaded.get(e['path'], '') + content
    # add the number of characters to the loaded text
    num_chars += len(content)
    # if the number of characters is reached, break the loop
    if num_chars >= args.num_chars:
        break
# join the files together and add 
html_output = ''
for key, value in loaded.items():
    html_output += f'<h1>[[{os.path.basename(key)}]]</h1>{value}<hr>'

# convert html to markdown
md_output = markdownify.markdownify(html_output)

# remove if exists
if os.path.exists('promised-victory/example.md'):
    os.remove('promised-victory/example.md')
# write to file
with open('promised-victory/example.md', 'w') as f:
    f.write(md_output)