import random

def getNew(ori):
	direc = random.randrange(0,4)
	#replace by letter on the left
	if direc == 0:
		return {
			'q':'w',
			'w':'q',
			'e':'w',
			'r':'e',
			't':'r',
			'y':'t',
			'u':'y',
			'i':'u',
			'o':'i',
			'p':'o',
			'a':'s',
			's':'a',
			'd':'s',
			'f':'d',
			'g':'f',
			'h':'g',
			'j':'h',
			'k':'j',
			'l':'k',
			'z':'x',
			'x':'z',
			'c':'x',
			'v':'c',
			'b':'v',
			'n':'b',
			'm':'n',
		}.get(ori,'')

	#replace by letter on the right
	elif direc == 1:
		return {
			'q':'w',
			'w':'e',
			'e':'r',
			'r':'t',
			't':'y',
			'y':'u',
			'u':'i',
			'i':'o',
			'o':'p',
			'p':'o',
			'a':'s',
			's':'d',
			'd':'f',
			'f':'g',
			'g':'h',
			'h':'j',
			'j':'k',
			'k':'l',
			'l':'k',
			'z':'x',
			'x':'c',
			'c':'v',
			'v':'b',
			'b':'n',
			'n':'m',
			'm':'n',
		}.get(ori,'')

	#replace by letter on the top
	elif direc == 2:
		return {
			'q':'a',
			'w':'s',
			'e':'d',
			'r':'f',
			't':'g',
			'y':'h',
			'u':'j',
			'i':'k',
			'o':'l',
			'p':'l',
			'a':'q',
			's':'w',
			'd':'e',
			'f':'r',
			'g':'t',
			'h':'y',
			'j':'u',
			'k':'i',
			'l':'o',
			'z':'a',
			'x':'s',
			'c':'d',
			'v':'f',
			'b':'g',
			'n':'h',
			'm':'j',
		}.get(ori,'')
	#replace by letter on the bottom
	else:
		return {
			'q':'a',
			'w':'s',
			'e':'d',
			'r':'f',
			't':'g',
			'y':'h',
			'u':'j',
			'i':'k',
			'o':'l',
			'p':'l',
			'a':'z',
			's':'x',
			'd':'c',
			'f':'v',
			'g':'b',
			'h':'n',
			'j':'m',
			'k':'m',
			'l':'m',
			'z':'a',
			'x':'s',
			'c':'d',
			'v':'f',
			'b':'g',
			'n':'h',
			'm':'j',
		}.get(ori,'')


def generateTypo():
	outf = open('./typo/typo.txt','w')

	with open('testData.txt','r') as f:
		for s in f:
			words = s.split()
			for word in words:
				ctype = random.randrange(0,4)
				pos = random.randrange(0,len(word))
				#add 
				if ctype == 0:
					letter = getNew(word[pos])
					shift = random.randrange(0,2)
					pos += shift
					word = word[:pos] + letter + word[pos:]
				#remove	a letter at random position
				elif ctype == 1:
					word = word[:pos] + word[pos+1:]
				#replace a letter with its neighbor 	
				elif ctype == 2:
					newLetter = getNew(word[pos])
					word = word[:pos] + str(newLetter) + word[pos+1:]
				#reorder
				else:
					letter = word[pos]
					word = word[:pos] + word[pos+1:]
					pos = random.randrange(0,len(word)+1)
					word = word[:pos] + letter + word[pos:]
				outf.write(word)
				outf.write(' ')
			outf.write('\n')

	outf.close()

				