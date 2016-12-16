import codecs
import jieba.posseg as pseg

fout = codecs.open('../data/describe.txt','w',encoding='utf8')
for line in open('../data/train_describe.txt','r'):
    seg_list = pseg.cut(line[:-1])
    for w in seg_list:
        fout.write(w.word+'/'+w.flag[:1]+' ')
    fout.write('\n')
fout.close()