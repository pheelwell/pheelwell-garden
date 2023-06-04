---
{"dg-publish":true,"permalink":"/technical/test-page/","noteIcon":"Technical","created":"2023-04-30T20:33:59.762+02:00","updated":"2023-06-04T16:42:09.311+02:00"}
---

On this Page I try stuff
## Python Scripts:

This project provides a set of Python scripts that help in generating, finding closest, and visualizing embeddings for a collection of notes. These scripts are particularly useful for processing and analyzing large sets of text data, such as notes or articles.

The Scripts can be found [here](https://github.com/pheelwell/pheelwell-garden/tree/master/research_scripts): 

### 1. `generate_embeddings.py`

This script generates embeddings for the provided notes in a specified folder.

**Usage:**

```bash
python generate_embeddings.py --path promised-victory --embeddings embeddings_v6.json --mode files --max_length 2000
```

**Arguments:**

- `--path`: The path to the folder containing the markdown files (default: 'promised-victory').
- `--embeddings`: The path to the output embeddings file (default: 'embeddings.json').
- `--mode`: The mode of processing - either 'files' or 'paragraphs' (default: 'files').
- `--max_length`: The maximum length of one embedding (default: 5000).

### 2. `get_closest_embeddings.py`

This script finds the closest embeddings to a given input text.

**Usage:**

```bash
python get_closest_embeddings.py --embeddings embeddings.json --num_chars 10000 --input_text "this is a test"
```

**Arguments:**

- `--embeddings`: The path to the input embeddings file (default: 'embeddings.json').
- `--num_chars`: The number of characters to load from the input file (default: 10000).
- `--input_text`: The input text that should be used to find the closest embeddings (required).

### 3. `vizualize_embeddings.py`

This script visualizes the generated embeddings using dimensionality reduction techniques with PCA and clustering with KMeans.

**Usage:**

```bash
python vizualize_embeddings.py --embeddings embeddings.json
```

**Arguments:**

- `--embeddings`: The path to the input embeddings file (default: 'embeddings.json').

### Example Workflow

1. Prepare a folder with markdown files containing your notes, e.g., 'promised-victory'.
2. Generate embeddings for these notes:

```bash
python generate_embeddings.py --path promised-victory --embeddings embeddings_v6.json --mode files --max_length 2000
```

3. Find the closest embeddings to a given input text:

```bash
python get_closest_embeddings.py --embeddings embeddings_v6.json --num_chars 10000 --input_text "this is a test"
```

4. Visualize the generated embeddings:

```bash
python vizualize_embeddings.py --embeddings embeddings_v6.json
```

![Pasted image 20230430203444.png](/img/user/resources/Pictures/Pasted%20image%2020230430203444.png)
![Pasted image 20230430203444.png| mix-blend-mode: lighten](/img/user/resources/Pictures/Pasted%20image%2020230430203444.png)

### 3. `vizualize_embeddings.py`

This script visualizes the generated embeddings using dimensionality reduction techniques with PCA and clustering with KMeans.

**Usage:**

```bash
python vizualize_embeddings.py --embeddings embeddings.json
```
