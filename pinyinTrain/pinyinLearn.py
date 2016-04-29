#coding: utf8
def remove(current):
	current = current.replace("ā","a")
	current = current.replace("á","a")
	current = current.replace("ǎ","a")
	current = current.replace("à","a")
	
	current = current.replace("ī","i")
	current = current.replace("í","i")
	current = current.replace("ǐ","i")
	current = current.replace("ì","i")

	current = current.replace("ē","e")
	current = current.replace("é","e")
	current = current.replace("ě","e")
	current = current.replace("è","e")

	current = current.replace("ō","o")
	current = current.replace("ó","o")
	current = current.replace("ǒ","o")
	current = current.replace("ò","o")	

	current = current.replace("ū","u")
	current = current.replace("ú","u")
	current = current.replace("ǔ","u")
	current = current.replace("ù","u")

	current = current.replace("ǖ","v")
	current = current.replace("ǘ","v")
	current = current.replace("ǚ","v")
	current = current.replace("ǜ","v")
	return current

def updateTranMap(preW,current,pinyinTran):
	if preW not in pinyinTran:
		pinyinTran[preW] = {}
	if current not in pinyinTran[preW]:
		pinyinTran[preW][current] = 1
	else:
		pinyinTran[preW][current] += 1

def pinyinLearnMethod():
	outf = open('./pinyinTrain/pinyinModel.txt','w')

	pinyinTran = {}
	with open('./pinyinTrain/pinyinTrainData.txt','r') as f:
		for line in f:
			words = line.strip().split()
			preW = ""
			for w in words:
				w = w.split('(')
				if ("。" in w[0]) or ("，" in w[0]) or ("！" in w[0]) or ("：" in w[0]) or ("？" in w[0]) or ("......" in w[0]) or ("、" in w[0]) or ('"' in w[0]) or ('；' in w[0]): 
					preW = ""
				if len(w) > 1:
					current = remove(w[1])
					updateTranMap(preW,current,pinyinTran)
					preW = current


	with open('./pinyinTrain/pinyinTrainData2.txt','r') as f:
		for line in f:
			words = line.strip().split()
			preW = ""
			for w in words:
				if ("。" in w) or ("，" in w) or ("！" in w) or ("：" in w) or ("？" in w) or ("......" in w) or ("、" in w) or ('"' in w) or ('“' in w) or ('”' in w) or ('；' in w): 
					preW = ""
				else:
					current = remove(w)
					updateTranMap(preW,current,pinyinTran)
					preW = current


	for word in pinyinTran:
		outf.write(word)
		outf.write('\n')
		for word2 in pinyinTran[word]:
			outf.write('%12s %12s' % (word2,str(pinyinTran[word][word2])))
			outf.write('\n')

	outf.close()
	print "Learning pinyin model finished."


