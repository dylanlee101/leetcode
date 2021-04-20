class Trie(object):
    def __init__(self):
        self.root = {}
        self.en_of_word = '#'

    def insert(self,word):
        node = self.root
        for char in word:
            node = node.setdefault(char,{})
        node[self.en_of_word] = self.en_of_word

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.en_of_word in node

    def startsWith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True