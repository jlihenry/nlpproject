import sys
import os
import fnmatch

outf = open('hmmmodel.txt','w')

tagwordDic = {}
transDic = {}
wordTag = {}


#for root,dirs,files in os.walk(sys.argv[1]):
#	for fileName in files:
#		if fnmatch.fnmatch(fileName,'*tagged*') and fileName.endswith(".txt"):
#			fullpath = os.path.join(root,fileName)

with open('RenMinData.txt','r') as f:
	line = f.readline().strip()
	while line:
		preTag = ""
		for tag in list(line.decode('utf-8')):
			if len(tag.strip())>0:
				tag = tag.encode('utf-8')
				if preTag in transDic:
					if tag in transDic[preTag]:
						transDic[preTag][tag] += 1
					else:
						transDic[preTag][tag] = 1
				else:
					transDic[preTag] = {}
					transDic[preTag][tag] = 1
		
				preTag = tag
		line = f.readline().strip()


with open('PinYin.txt','r') as f:
	for line in f:
		if len(line.strip()) > 0:
			word = line.strip().split()
			tag = word[0].decode('utf-8').encode('utf-8')
			words = [py[0:-1] for py in word[1:]]
			for keyword in words:
				if tag in tagwordDic:
					if keyword in tagwordDic[tag]:
						tagwordDic[tag][keyword] += 1
					else:
						tagwordDic[tag][keyword] = 1
				else:
					tagwordDic[tag] = {}
					tagwordDic[tag][keyword] = 1
				if keyword not in wordTag:
					wordTag[keyword] = set()
				wordTag[keyword].add(tag)


for tag in tagwordDic:
	outf.write(tag)
	outf.write('\n')
	for word in tagwordDic[tag]:
		outf.write('%12s %12s' % (word,str(tagwordDic[tag][word])))
		outf.write('\n')

outf.write("\n#transDic#\n\n")

for preTag in transDic:
	outf.write(preTag)
	outf.write('\n')
	for postTag in transDic[preTag]:
		outf.write('%12s %12s' % (postTag,str(transDic[preTag][postTag])))
		outf.write('\n')

outf.write("\n#wordTag#\n\n")

for word in wordTag:
	outf.write(word)
	outf.write(' ')
	for tag in wordTag[word]:
		outf.write(tag)
		outf.write(' ')
	outf.write('\n')		

outf.close()

