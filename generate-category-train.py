# coding: utf8
import codecs
import json

datafile = '../data/taobao_trial_result.txt'
category_dict = dict()
s = set()
cnt = 0
fout = codecs.open('../data/train_describe.txt', 'w', encoding='utf8')
for line in open(datafile, 'r'):
    info = json.loads(line)
    for item in info['taobao_orders']:  # each item
        try:
            if ('describe' in item) and (item['describe'] not in s):
                fout.write(item['describe'])
                fout.write('\n')
                s.add(item['describe'])
        except:
            print item
    cnt += 1
    print cnt, len(s)
fout.close()