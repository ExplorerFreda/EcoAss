# coding: utf8

import json
import codecs

iw = json.loads(codecs.open('../data/industryWord.json',encoding='gbk').readline())
category = dict()
for item in iw['data']:
    category[item['primInduName']] = item['primInduCode']
    for secItem in item['secList']:
        category[secItem['secnduName']] = secItem['secInduCode']
        print secItem['secnduName']
fout = codecs.open('../data/company_field_info_withcategory_gbk.csv', 'w', encoding='gbk')
fout.write('id,company_name,field,categoryCode\n')
for line in codecs.open('../data/company_field_info.csv',encoding='gbk').readlines()[1:]:
    id = line[:line.find(',')]
    field = line[line.rfind(',')+1:-1]
    name = line[line.find(',')+1:line.rfind(',')]
    if name.find(',') != -1:
        name = '"' + name + '"'
    if field in category:
        categorycode = category[field]
    else:
        if field != 'NULL' and field != 'CannotFind':
            print 'Error', field
        categorycode = 'NULL'
    print id, name, field, categorycode
    fout.write(id + ',' + name + ',' + field + ',' + categorycode + '\n')
fout.close()