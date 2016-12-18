import codecs
import json


def load_kmeans_result(filename):
	ret = dict()
	for line in codecs.open(filename, 'r', encoding='utf8'):
		[word, cluster] = line.split()
		cluster = int(cluster)
		ret[word] = cluster
	return ret


def save_kmeans_result(kmeans, filename):
	fout = codecs.open(filename, 'w', encoding='utf8')
	items = [(x,kmeans[x]) for x in kmeans]
	items = sorted(items, key=lambda x:x[1])
	for item in items:
		fout.write(item[0] + ' ' + str(item[1]) + '\n')
	fout.close()



kmeans = load_kmeans_result('../../data/kmeans_result.txt')
save_kmeans_result(kmeans, '../../data/kmeans_result_sorted_cluster.txt')

description_filename = '../../data/describe.txt'
description_embedding_filename = '../../data/description_embedding.txt'
fout = codecs.open(description_embedding_filename, 'w', encoding='utf8')
for line in codecs.open(description_filename, encoding='utf8'):
	words = line.split()
	cluster_set = dict()
	for word in words:
		if word not in kmeans:
			continue
		if kmeans[word] not in cluster_set:
			cluster_set[kmeans[word]] = 0
		cluster_set[kmeans[word]] += 1
	fout.write(json.dumps(cluster_set) + '\n')
fout.close()
