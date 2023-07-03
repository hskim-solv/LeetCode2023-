class Trie:

    def __init__(self):
        self.stack = []
        

    def insert(self, word: str) -> None:
        self.stack.append(word)

    def search(self, word: str) -> bool:
        if word in self.stack:
            return True

    def startsWith(self, prefix: str) -> bool:
        for word in self.stack:
            if word.startswith(prefix):
                return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)