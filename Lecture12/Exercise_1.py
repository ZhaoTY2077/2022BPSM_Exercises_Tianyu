for line in open("input.txt"):
	adaptor = line[0:14]
	newseq = line.replace(adaptor,"")
	print(len(newseq))
	print(newseq)
