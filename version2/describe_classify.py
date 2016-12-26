import codecs
import json

describe_filename = '../../data/describe.txt'
cluster_filename = '../../data/kmeans_result_sorted_cluster.txt'
output_filename = '../../data/describe_type.txt'
flog = codecs.open('log.txt','w','utf8')

# find corresponding category for each cluster
cluster = dict()
cluster_to_category = dict()
for line in codecs.open(cluster_filename,'r','utf8'):
	[word, clus] = line.split()
	pos = word.rfind('/')
	word = word[:pos]
	clus = int(clus)
	cluster[word] = clus
cluster_category_score = [[0 for i in range(13)] for j in range(200)]
for category in range(13):
	wordlist_filename = '../../data/sample_words_new/%d.txt'%category
	for line in codecs.open(wordlist_filename, 'r', 'utf8'):
		pos = line.find('/')
		word = line[:-2]
		if word not in cluster:
			continue
		cluster_category_score[cluster[word]][category] += 1
for i in range(200):
	maxcnt = 0
	argmax = -1
	for j in range(13):
		if maxcnt < cluster_category_score[i][j]:
			maxcnt = cluster_category_score[i][j]
			argmax = j
	cluster_to_category[i] = argmax
for line in open('cates.txt'):
	clus, cate = line.split()
	clus = int(clus)
	cate = int(cate)
	cluster_to_category[clus] = cate
print cluster_to_category
flog.write(json.dumps(cluster_to_category)+'\n')

fout = codecs.open(output_filename,'w','utf8')

for cnt, line in enumerate(codecs.open(describe_filename,'r','utf8')):
	words = line.split()
	newline = ''
	weight = [0 for i in range(13)]
	for word in words:
		word = word[:word.rfind('/')]
		newline += word
		if word in cluster and cluster_to_category[cluster[word]]!=-1:
			weight[cluster_to_category[cluster[word]]] += 1
	maxcnt = 0
	argmax = -1
	for i in range(13):
		if maxcnt < weight[i]:
			maxcnt = weight[i]
			argmax = i
	if cnt % 1000 == 0:
		print cnt
	if newline == '':
		continue
	fout.write(newline + ' ' + str(argmax) + '\n')

fout.close()
flog.close()
