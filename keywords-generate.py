# coding: utf8
import codecs
import json
from collections import Counter

datafile = '../data/describe.txt'
cnt = Counter()
for line in codecs.open(datafile, 'r', encoding='utf8'):
    for word in line.split():
        cnt[word] += 1
print len(cnt)
fout = codecs.open('../data/keywords.txt', 'w', encoding='utf8')
wordlist = []
for word in cnt:
    wordlist.append((word, cnt[word]))
wordlist = sorted(wordlist, key=lambda x:x[1])
wordlist.reverse()  # sort all keywords by frequency
tag = dict()    # type tag for each keyword
                # 0: cannot determine by this word
                # 1: necessity
                # 2: non-necessity
                # 3: luxury
                # 4: game related
for word in wordlist:
    fout.write(word[0] + ' ' + str(word[1]) + '\n')
fout.close()