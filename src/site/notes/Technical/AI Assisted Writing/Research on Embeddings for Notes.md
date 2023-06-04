---
{"dg-publish":true,"permalink":"/technical/ai-assisted-writing/research-on-embeddings-for-notes/","noteIcon":"Technical","created":"2023-04-10T20:06:31.233+02:00","updated":"2023-06-04T16:38:11.088+02:00"}
---

This project explores the use of embeddings to analyze and organize a collection of notes. The process involves generating embeddings for the notes, finding the closest embeddings to a given input text, and visualizing the generated embeddings.

The workflow consists of three Python scripts:

1. `generate_embeddings.py` - Generates embeddings for notes in a specified folder.
2. `get_closest_embeddings.py` - Finds the closest embeddings to a given input text.
3. `vizualize_embeddings.py` - Visualizes the generated embeddings using PCA or t-SNE.

An example workflow can be found in the provided Python scripts section.

## Findings
During this research, several observations were made:

- Storing vectors in JSON files is efficient, as it takes only about 2 seconds to find nearest vectors and write content.
- Separating notes by headings may result in less informative vectors for short headings. Adding metadata or using a two-stage approach (finding best-fitting documents first) could help improve results. 
- The stored Vector Json is 25MB
- Excluding indexed notes might be necessary, as templates can interfere with queries.

Visualizations of clustered embeddings revealed some interesting patterns:

- Including filenames in the analysis seemed to have a significant impact on grouping, which may be beneficial or detrimental depending on the desired outcome.
- Removing empty files and enforcing a minimum character count (e.g., 100 characters) improved clustering quality.
- Clusters of research articles, documentation, and other content types were observed in the visualizations.

The following images showcase some visualizations from this research:
