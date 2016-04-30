# if everything works fine,
# pls delete the debug prompt lines in search_pinyin_dfs
# all you need to use is insert_PinYin(str) and search_PinYin(str)


class TrieNode:

	def __init__(self):
		self.isPinYin = False 
		self.child = {}

class Trie:

	def __init__(self):
		# everytime we add a new pinyin in the trie, we put the current pinyin in this list.
		# if pinyin already in this list, we dont add it into the trie
		self.PinYin_Set = []
		self.root = TrieNode()
		self.key_modify_set = {}
		self.init_key_modify_set()
		self.max_MatchVal = 0;

	# the letter user will make mistake, a e i o u g r h
	def init_key_modify_set(self):
		dic = {}
		dic['s'] = 'a'
		dic['w'] = 'e'
		dic['r'] = 'e'
		dic['u'] = 'i'
		dic['o'] = 'i'
		dic['i'] = 'o'
		dic['p'] = 'o'
		dic['y'] = 'u'  # we assume that only y map to u. dont consider i
		dic['f'] = 'g'
		dic['h'] = 'g'
		dic['e'] = 'r'
		dic['t'] = 'r'
		dic['g'] = 'h'
		dic['j'] = 'h'
		dic['b'] = 'n'
		dic['m'] = 'n'
		self.key_modify_set = dic


	# print all PinYins in the trie
	def traverse(self):
		print '*' * 10
		print "PinYin_Set:"
		for str in self.PinYin_Set:
			print str
		print '*' * 10
		print "in trie, we get :"
		self.traverse_dfs("", self.root)
		print '*' * 10

	def traverse_dfs(self, str, node):

		if node.isPinYin == True:
			pass
			#print str
		for c in node.child:
			self.traverse_dfs(str + c, node.child[c])

    # try add a pinyin into trie, if already in PinYin_set, then do nothing
	def insert_PinYin(self, str):
		
		if str not in self.PinYin_Set:
			
			self.PinYin_Set.append(str)

			curNode = self.root
			for c in str:
				if c not in curNode.child:
					curNode.child[c] = TrieNode()
				curNode = curNode.child[c]
			curNode.isPinYin = True

	#with the given str, 
	#return a List filled with possible pinyins from the trie.
	def search_PinYin(self, search_str):

		ans = []
		self.search_PinYin_dfs(self.root, 0, search_str, "", ans)
		return ans

    # do the pinyin correction things, add possible pinyins into the ans
	def search_PinYin_dfs(self, node, index, search_str, 
						  cur_str, ans):
		
		# reach the end of the str, check if search_str is a pinyin
		if index == len(search_str):
			if node.isPinYin == True : 
				ans.append(cur_str)
			else:
				#print "%s in trie, but not a PinYin" % search_str
				self.get_PinYin_from_children(node, cur_str, ans)
			return 

		cur_letter = search_str[index]

		# cur_letter not in node.child, user make misktake when input pinYin
		# do the pinyin correction algorithm
		if cur_letter not in node.child:
			
			#print "letter %r is not in the trie, try to modify" % cur_letter

			# do the keyboard word modification 
			if cur_letter in self.key_modify_set and self.key_modify_set[cur_letter] in node.child:
				#print "change letter %r to %r" % (cur_letter, self.key_modify_set[cur_letter])
				cur_letter = self.key_modify_set[cur_letter]

				self.search_PinYin_dfs(node.child[cur_letter], index + 1, search_str,
						       cur_str + cur_letter, ans)


			#find the most matching pinyins
			else:
				#print "cannot modify letter %r with key_modify_set" % cur_letter
				#print "find the most matching one start from cur node"	

				self.max_MatchVal = 0

				self.get_matching_pinyin(node, cur_str, search_str, 0, ans)
				

		# cur_letter in node.child, keep going the basic algorithm
		else:
			self.search_PinYin_dfs(node.child[cur_letter], index + 1, search_str,
						       cur_str + cur_letter, ans)


	def get_matching_pinyin(self, node, cur_str, search_str, cur_matchVal, ans):

		# if curMatchval larger than maxVal, clear the ans
		if cur_matchVal > self.max_MatchVal:
			del ans[:]
			self.max_MatchVal = cur_matchVal

		# if cur_str is Pinyin && curVal == Maxval, append cur Pinyin into ans
		if node.isPinYin is True and cur_matchVal == self.max_MatchVal: 
			ans.append(cur_str)

		# travers all child below cur node
		for letter in node.child:

			#letter is in search_str, curval increment by 1
			if letter in search_str:
				cur_matchVal += 1

			self.get_matching_pinyin(node.child[letter], cur_str + letter, search_str, cur_matchVal, ans)



	def get_PinYin_from_children(self, node, cur_str, ans):

		if node.isPinYin == True:
			ans.append(cur_str)

		for c in node.child :
			self.get_PinYin_from_children(node.child[c], cur_str + c, ans)

