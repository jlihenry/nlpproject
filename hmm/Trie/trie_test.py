from trie import *


## a prompt function to check the answer of search
def search(str,trie):
	print "search: %s" % str
	print trie.search_PinYin(str)

trie = Trie()

#test if a word in a trie, if word is not a pinyin, print all the pinyin children below
'''
search("a", trie)
search("b", trie)
search("be", trie)

trie.traverse()

trie.insert_PinYin("ab")
trie.insert_PinYin("abc")
trie.insert_PinYin("abd")
trie.insert_PinYin("bea")
trie.insert_PinYin("bc")
'''

'''
#test keyword modify function
trie.insert_PinYin("leng")
trie.insert_PinYin("li")
trie.insert_PinYin("long")

trie.traverse()

search("liu", trie)
search("liy",trie)
search("l",trie)
search("lomh",trie)
'''

#test find the most matching one

trie.insert_PinYin("le")
trie.insert_PinYin("leg")
trie.insert_PinYin("log")


trie.traverse()

search("lgo",trie)


