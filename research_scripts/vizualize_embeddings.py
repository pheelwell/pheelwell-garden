import json
import plotly.graph_objs as go
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import argparse
import os
# argparse
# example usage:
# python vizualize_embeddings.py --embeddings embeddings.json --output output.html
parser = argparse.ArgumentParser()
parser.add_argument('--embeddings', type=str, default='embeddings.json', help='path to embeddings file')
parser.add_argument('--output', type=str, default='output.html', help='path to output file')
args = parser.parse_args()

type_to_emoji = {
    'Meta': '⚙️',
    'Locality': '🏠',
    'NPC': '👤',
    'History': '📅',
    'Arc': '📖',
    'Plot': '📜',
    'Scene': '🎬',
    'Thing': '🔮',
    'Faction': '⚔️',
    'Region': '🗺',
    'Settlement': '🏰'
}
    

# Load embeddings from file
with open(args.embeddings, 'r') as f:
    embeddings_data = json.load(f)

# Extract embeddings and file names
embeddings = [d['embeddings'] for d in embeddings_data]
filenames = [d['path'] for d in embeddings_data]

# Project embeddings into 3D space using PCA
pca = PCA(n_components=3)
embeddings_3d = pca.fit_transform(embeddings)


# Cluster embeddings
n_clusters = 10
kmeans = KMeans(n_clusters=n_clusters, random_state=43).fit(embeddings)
labels = kmeans.labels_
# other method for clustering: DBSCAN
#from sklearn.cluster import DBSCAN
#labels = DBSCAN(eps=0.3, min_samples=10).fit_predict(embeddings)
print (labels)

# Create a scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=[e[0] for e in embeddings_3d],
    y=[e[1] for e in embeddings_3d],
    z=[e[2] for e in embeddings_3d],
    mode='markers',
    marker=dict(
        color=labels,  # <-- Add color parameter with the labels
        size=5,
        opacity=0.8,
        colorscale='Viridis'
    ),
    # only use basename
    text=[os.path.basename(f) for f in filenames],
    hovertemplate='%{text}',
    hoverlabel=dict(
        bgcolor='white',
        font_size=16,
        font_family='Rockwell'
    ),
)])

# Customize layout
fig.update_layout(
    title='Embeddings Clustering',
    scene=dict(
        xaxis=dict(title='Dimension 1'),
        yaxis=dict(title='Dimension 2'),
        zaxis=dict(title='Dimension 3')
    )
)

# Save plot
fig.write_html(args.output)

