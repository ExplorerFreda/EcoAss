import codecs
from sklearn.cluster import KMeans
import numpy as np


filename = '../../data/embeddings.txt'
kmeans_result = '../../data/kmeans_result.txt'
vectors = []
words = []
for line in codecs.open(filename, encoding='utf8'):
	if len(line.split()) < 50:
		continue
	word = line.split()[0]
	vector = [float(x) for x in line.split()[1:]]
	vectors.append(vector)
	words.append(word)

X = np.array(vectors)
kmeans = KMeans(n_clusters = 200, random_state = 0).fit(X)
labels = kmeans.labels_


fout = codecs.open(kmeans_result, 'w', encoding='utf8')
for i in range(len(words)):
	fout.write(words[i] + '\t' + str(labels[i]) + '\n')
fout.close()

