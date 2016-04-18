import sys
import os
import fnmatch
import math

transDic = {}
tagwordDic = {}
wordTag = {}
flag = 0
currentKey = ''

with open('hmmmodel.txt','r') as f:
	for s in f:
		data = s.split()
		if flag == 0:
			if len(data) == 1:
				if data[0] == '#transDic#':
					flag = 1
					currentKey = ''
					transDic[currentKey] = {}
					transDic[currentKey]['total'] = 0
				else:
					data[0] = data[0].decode('utf-8').encode('utf-8')
					tagwordDic[data[0]] = {}
					tagwordDic[data[0]]['total'] = 0
					currentKey = data[0]
			elif(len(data) == 2):
				tagwordDic[currentKey][data[0]] = int(data[1])
				tagwordDic[currentKey]['total'] += int(data[1])
		elif flag == 1:
			if len(data) == 1:
				if data[0] == '#wordTag#':
					flag = 2
				else:
					data[0] = data[0].decode('utf-8').encode('utf-8')
					transDic[data[0]] = {}
					transDic[data[0]]['total'] = 0
					currentKey = data[0]
			elif(len(data) == 2):
				data[0] = data[0].decode('utf-8').encode('utf-8')
				transDic[currentKey][data[0]] = int(data[1])
				transDic[currentKey]['total'] += int(data[1])
		else:
			if len(data) > 1:
				if data[0] not in wordTag:
					wordTag[data[0]] = set()
				for i in range(1,len(data)):
					wordTag[data[0]].add(data[i].decode('utf-8').encode('utf-8'))
	

with open('testData.txt','r') as f:
	for s in f:
		words = s.split()
		wordTagDic = {}
		wordTagDic[0] = {}
		wordTagDic[0][''] = {}
		wordTagDic[0]['']['prob'] = math.log10(1)
		#preTag = {}
		#preTag[''] = math.log10(1)
		for i in range(1,len(words)+1):
			word = words[i-1]
			#currentTag = set()
			wordTagDic[i] = {}
			for tag in wordTagDic[i-1]:
				if word not in wordTag:
					wordTag[word] = set()
					for tagNew in tagwordDic:
						wordTag[word].add(tagNew)
						tagwordDic[tagNew][word] = tagwordDic[tagNew]['total']
				for ctag in wordTag[word]:
					if tag not in transDic or ctag not in transDic[tag]:
						continue
					else:
						temp = wordTagDic[i-1][tag]['prob'] + math.log10(transDic[tag][ctag]) - math.log10(transDic[tag]['total']) + math.log10(tagwordDic[ctag][word]) - math.log10(tagwordDic[ctag]['total'])
						if ctag not in wordTagDic[i]:
							#currentTag.add(ctag)
							wordTagDic[i][ctag] = {}
							wordTagDic[i][ctag]['pre'] = tag
							wordTagDic[i][ctag]['prob'] = temp
						else:
							if temp > wordTagDic[i][ctag]['prob']:
								wordTagDic[i][ctag]['prob'] = temp
								wordTagDic[i][ctag]['pre'] = tag 
			#transition is 0
			if len(wordTagDic[i]) == 0:
				for tag in wordTagDic[i-1]:
					for ctag in wordTag[word]:
						wordTagDic[i][ctag] = {}
						wordTagDic[i][ctag]['prob'] = 0
						wordTagDic[i][ctag]['pre'] = tag

		j = len(words)
		output = ""
		finalTag = ''
		maxProb = -sys.maxint-1
		for tag in wordTagDic[j]:
			if finalTag == '' or maxProb < wordTagDic[j][tag]['prob']:
				finalTag = tag
				maxProb = wordTagDic[j][tag]['prob']
		while j > 0:
			output = str(finalTag) + ' ' + output
			finalTag = wordTagDic[j][finalTag]['pre']
			j -= 1
		print output
		print '\n'






