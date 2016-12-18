import codecs


# cmd = w: with POSTag; o: without POSTag
def load_similarity(filename, cmd = 'w'):
	fin = codecs.open(filename, encoding='utf8')
	ret = dict()
	while True:
		line = fin.readline()
		if len(line) < 2:
			break
		if cmd == 'w':
			line = line[:-1]
		elif cmd == 'o':
			line = line[:line.rfind('/')]
		if line in ret:
			print line
		ret[line] = []
		for i in range(10):
			[word, sim] = fin.readline().split()
			if cmd == 'o':
				word = word[:word.rfind('/')]
			sim = float(sim)
			ret[line].append((word, sim))
	return ret


