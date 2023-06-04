---
{"dg-publish":true,"permalink":"/technical/ai-assisted-writing/research-on-embeddings-for-notes/","noteIcon":"Technical","created":"2023-04-10T20:06:31.233+02:00","updated":"2023-06-04T16:39:41.742+02:00"}
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

1. Clustering for embeddings for each seperate heading with filenames attached:
![Pasted image 20230410220445.png](/img/user/resources/Pictures/Pasted%20image%2020230410220445.png)
2. Clustered paragraph embeddings without filenames:
![Pasted image 20230411001417.png](/img/user/resources/Pictures/Pasted%20image%2020230411001417.png)
3. Weird Vector from empty File, Embeddings done on whole files:
![Pasted image 20230410222154.png](/img/user/resources/Pictures/Pasted%20image%2020230410222154.png)
4. Improved clustering after removing empty files and enforcing a 100-character minimum:
![Pasted image 20230410222510.png](/img/user/resources/Pictures/Pasted%20image%2020230410222510.png)
5. Zoomed-in view showing a cluster of research articles:
![Pasted image 20230410222553.png](/img/user/resources/Pictures/Pasted%20image%2020230410222553.png)
6. Zoomed-in view showing a cluster of documentation:
![Pasted image 20230410222621.png](/img/user/resources/Pictures/Pasted%20image%2020230410222621.png)
7. Only Fantasy Prompts:
 ![Pasted image 20230411001703.png](/img/user/resources/Pictures/Pasted%20image%2020230411001703.png)
In conclusion, this research demonstrates the potential of using embeddings to analyze and organize notes, revealing patterns and relationships that can be further explored or leveraged for practical applications.

## Example Usage:
As an example of practical usage, this approach was used to generate a list of interesting secrets for a fictional campaign by appending relevant prompts to an output file and running it through GPT-4. This resulted in this query output containing all important Articles:
[[Technical/AI Assisted Writing/Secret Query Output File\|Secret Query Output File]]
The output was appended by "Give a list of the most important Secerts of the Campain". This was the Result given by GPT-4:
[[Technical/AI Assisted Writing/Important Secrets of the Campain\|Important Secrets of the Campain]]
