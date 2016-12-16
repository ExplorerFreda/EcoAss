import codecs
import json

describe = codecs.open('../data/train_describe.txt','r',encoding='utf8').readlines()
describe = [line[:-1] for line in describe]
tag = codecs.open('../data/tags_by_description.txt').readlines()
tag = [int(x[:-1]) for x in tag]
des_tag = dict()
for i in range(len(tag)):
    des_tag[describe[i]] = tag[i]
print 'Load info done.'

cnt = 0
datafile = '../data/taobao_trial_result.txt'
fout = codecs.open('../data/personal_info.txt', 'w')
for line in open(datafile, 'r'):
    info = json.loads(line)
    person_info = dict()
    person_info['cid'] = info['cid']
    for item in info['taobao_orders']:  # each item
        try:
            if 'trans_time' not in item or 'price' not in item:
                print 'Oh No!'
                continue
            time = item['trans_time'].split()[0]
            money = item['price']
            if time not in person_info:
                person_info[time] = [0, 0, 0, 0, 0, 0]
            if ('describe' in item) and (item['describe'] in des_tag):
                person_info[time][des_tag[item['describe']]] += money
        except:
            print item
    cnt += 1
    print cnt
    fout.write(json.dumps(person_info) + '\n')
fout.close()