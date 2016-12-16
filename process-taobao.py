# coding: utf8
import codecs
import json

datafile = '../data/taobao_trial_result.txt'
for line in open(datafile, 'r'):
    info = json.loads(line)
    print line
    for item in info['taobao_orders']:  # each item
        print item['type']


    break