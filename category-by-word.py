import codecs
import numpy as np

numtype = 5


def load_tagged_keywords():
    dic = [set() for x in range(numtype)]
    for i in range(numtype):
        fin = codecs.open('../data/sample_words/%d.txt'%i,'r',encoding='utf8')
        for line in fin:
            dic[i].add(line[:-2])
            if line[-3]>'z' or line[-3]<'a':
                print 'error', i, line, line[-3]
    return dic


def save_tags(filename):
    fout = codecs.open(filename, 'w', encoding='utf8')
    for x in product_tag:
        fout.write(str(x) + '\n')
    fout.close()


datafile = '../data/describe.txt'
product_tag = [numtype for x in open(datafile)]
tag_keywords = load_tagged_keywords()
while True:
    determined = 0
    poly = 0
    for iter, line in enumerate(codecs.open(datafile, 'r', encoding='utf8')):
        if product_tag[iter] != numtype:
            continue
        flag = [0 for i in range(numtype)]
        for word in line.split():
            for j in range(numtype):
                if word in tag_keywords[j]:
                    flag[j] = 1
        if np.sum(flag) == 1:
            for j in range(numtype):
                if flag[j] == 1:
                    product_tag[iter] = j
            determined += 1
        elif np.sum(flag) > 1:
            for j in range(numtype):
                if flag[j] == 1:
                    product_tag[iter] = j
            determined += 1
        else:
            print line
        if iter % 10000 == 0:
            print iter
    save_tags('../data/tags_by_description.txt')
    break
print determined, poly, determined+poly
