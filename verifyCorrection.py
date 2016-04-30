from __future__ import division
from typo.typoGenerator import *
from hmm.Trie.trie import *
from hmm.hmmdecode import *


generateTypo()
pinyinTrans = {}
trie = Trie()
learnPinyinModel(pinyinTrans,trie)


originalWords = {}
with open('testData.txt','r') as f:
	originalWords = f.read().split()

i = 0
count = 0
with open('./typo/typo.txt','r') as f:
	for line in f:
		preWord = ""
		words = line.split()
		for word in words:
			wordCandidate = trie.search_PinYin(word)
			if len(wordCandidate) > 0:
				word = wordCandidate[0]
				maxP = 0
				if preWord in pinyinTrans:
					for wordCan in wordCandidate:
						if (wordCan in pinyinTrans[preWord]) and (pinyinTrans[preWord][wordCan] > maxP):
							maxP = pinyinTrans[preWord][wordCan] 
							word = wordCan
			if word == originalWords[i]:
				count += 1
			i += 1

print 1 - count / i

