# coding: utf8
import codecs
import json
from collections import Counter
import winsound
import numpy as np

used_keyword_set = set()
product_tag = [0 for i in range(len(open('../data/describe.txt').readlines()))]


def generate_keywords():
    datafile = '../data/describe.txt'
    cnt = Counter()
    for iter,line in enumerate(codecs.open(datafile, 'r', encoding='utf8')):
        if product_tag[iter] != 0:
            continue
        for word in line.split():
            if word not in used_keyword_set:
                cnt[word] += 1
    print len(cnt)
    wordlist = []
    for word in cnt:
        if word[-1] == 'n':
            wordlist.append((word, cnt[word]))
    wordlist = sorted(wordlist, key=lambda x:x[1])
    wordlist.reverse()  # sort all keywords by frequency
    wordlist = wordlist[:min(20, len(wordlist))]
    for word in wordlist:
        used_keyword_set.add(word[0])
    return wordlist


def add_tags(wordlist, tags):
    if len(wordlist) != len(tags):
        print 'Error: length invalid.'
    dic = dict()
    for iter in range(len(tags)):
        dic[wordlist[iter][0]] = tags[iter]
    datafile = '../data/describe.txt'
    for iter,line in enumerate(codecs.open(datafile, 'r', encoding='utf8')):
        if product_tag[iter] != 0:
            continue
        for word in line.split():
            if (word in dic) and product_tag[iter]==0 and dic[word]!=0:
                product_tag[iter] = dic[word]
                break
    return np.sum([t==0 for t in product_tag])


def save_tags(filename):
    fout = codecs.open(filename, 'w', encoding='utf8')
    for x in product_tag:
        fout.write(str(x) + '\n')
    fout.close()


tag = dict()    # type tag for each keyword
                # 0: cannot determine by this word
                # 1: necessity
                # 2: non-necessity
                # 3: luxury
                # 4: game related
while True:
    wordlist = generate_keywords()  # generate the most frequent key words
    winsound.Beep(500, 2000)
    tags = []
    for word in wordlist:
        tags.append(int(raw_input(word[0] + ' ' + str(word[1]) + '\n')))
    print add_tags(wordlist, tags), 'products not determined'
    save_tags('../data/tags_by_description.txt')
