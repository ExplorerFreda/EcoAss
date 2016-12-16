import codecs
import numpy as np

def load_tagged_keywords():
    dic = [set() for x in range(5)]
    for i in range(5):
        fin = codecs.open('../data/sample_words/%d.txt'%i,'r',encoding='utf8')
        for line in fin:
            dic[i].add(line[:-2])
            if line[-3]>'z' or line[-3]<'a':
                print 'error', i, line, line[-3]
    return dic


def load_keywords():
    words = []
    for line in codecs.open('../data/keywords.txt','r',encoding='utf8'):
        word = line.split()[0]
        if word[-1] == 'x':
            continue
        words.append(word)
    return words


keywords = load_keywords()
prob = dict()
print len(keywords)
for word in keywords:
    prob[word] = [0, 0, 0, 0, 0]
tagged = load_tagged_keywords()
for tag in range(len(tagged)):
    for word in tagged[tag]:
        prob[word][tag] = 1

for iteration in range(200):
    print 'iter', iteration, 'begins'
    prob_copy = dict()
    for word in prob:
        prob_copy[word] = prob[word]
        prob[word] = [0, 0, 0, 0, 0]
    for item, line in enumerate(codecs.open('../data/describe.txt','r',encoding='utf8')):
        words = line.split()
        p = [0, 0, 0, 0, 0]
        for word in words:
            if word not in keywords:
                continue
            for i in range(5):
                p[i] += prob_copy[word][i]
        for word in words:
            if word not in keywords:
                continue
            for i in range(5):
                prob[word][i] += p[i]
        if item % 100 == 0:
            print item
    for word in prob:
        sump = np.sum(prob[word])
        for i in range(4):
            prob[w][i] /= sump
    print 'iter', iteration, 'done'
    fout = codecs.open('../data/keywordprob.txt')
    for word in prob:
        fout.write(word + ' ' + str(prob[word][0]) + str(prob[word][1]) + ' '
                   + str(prob[word][2]) + ' ' + str(prob[word][3]) + '\n')
    fout.close()