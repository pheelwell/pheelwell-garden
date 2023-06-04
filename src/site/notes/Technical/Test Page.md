---
{"dg-publish":true,"permalink":"/technical/test-page/","noteIcon":"Technical","created":"2023-04-30T20:33:59.762+02:00","updated":"2023-06-04T16:46:02.840+02:00"}
---


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


## Python Scripts:

This project provides a set of Python scripts that help in generating, finding closest, and visualizing embeddings for a collection of notes. These scripts are particularly useful for processing and analyzing large sets of text data, such as notes or articles.

The Scripts can be found [here](https://github.com/pheelwell/pheelwell-garden/tree/master/research_scripts): 

### 1. `generate_embeddings.py`

This script generates embeddings for the provided notes in a specified folder.

**Usage:**

```bash
python generate_embeddings.py --path promised-victory --embeddings embeddings_v6.json --mode files --max_length 2000
```
