import gensim
import codecs
import json


corpus_filename = '../../data/describe.txt'
word_embedding_filename = '../../data/embeddings.txt'
similarity_result = '../../data/similarity.txt'


model = gensim.models.Word2Vec.load_word2vec_format(word_embedding_filename, binary=False)
fout = codecs.open(similarity_result, 'w', encoding='utf8')
cnt = 0
for word in model.vocab:
	fout.write(word + '\n')
	similar_words = model.most_similar(word)
	for item in similar_words:
		fout.write('\t'+item[0]+' '+str(item[1])+'\n')
	cnt += 1
	if cnt % 1000 == 0:
		print cnt, len(model.vocab)
fout.close()
