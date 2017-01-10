# This script is used to classify matched csv

import codecs
import json
import jieba.posseg as pseg

describe_type_filename = '../../data/describe_type.txt'
cluster_filename = '../../data/kmeans_result_sorted_cluster.txt'
input_filename = '../../data/matched_tb.csv'
output_filename = '../../data/matched_tb_with_category.csv'

# load_types 
cluster_to_category = json.loads(codecs.open('cates_whole.txt','r','utf8').readline())
cluster_to_category_temp = dict()
for item in cluster_to_category:
	cluster_to_category_temp[int(item)] = cluster_to_category[item]
cluster_to_category = cluster_to_category_temp
cluster = dict()
for line in codecs.open(cluster_filename,'r','utf8'):
	[word,clus] = line.split()
	pos = word.rfind('/')
	word = word[:pos]
	clus = int(clus)
	cluster[word] = clus


def get_taobao_desc_type(desc):
	if type(desc) != type(u'inicode-string'):
		return '-1'
	words = [word.word for word in pseg.cut(desc)]
	weight = [0 for i in range(14)]
	for word in words:
		if word in cluster:
			if cluster_to_category[cluster[word]]== -1:
				continue
			weight[cluster_to_category[cluster[word]]] += 1
	maxcnt = 0
	argmax = -1
	for i in range(14):
		if maxcnt < weight[i]:
			maxcnt = weight[i]
			argmax = i
	return str(argmax)


fout = codecs.open(output_filename, 'w', 'utf8')
for cnt, line in enumerate(codecs.open(input_filename, 'r', 'utf8')):
	if cnt > 2000000:
		break
	items = line.split('&*(@#!$')
	if len(items[4]) > 0 and items[4] != 'None':
		desc = items[4]
	else:
		desc = items[5]
	category = get_taobao_desc_type(desc)
	items[-1] = category
	output = '&*(@#!$'.join(items)
	fout.write(output+'\n')
	if cnt % 1000 == 0:
		print cnt
fout.close()

