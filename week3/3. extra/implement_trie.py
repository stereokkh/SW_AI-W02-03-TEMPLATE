class Node:
    children : dict[str, "Node"]
    is_end : bool
    def __init__(self, is_end = False, children = {}):
        self.children = children
        self.is_end = is_end
        pass


class Trie:

    def __init__(self, ):
        self.node = Node()
        

    def insert(self, word: str) -> None:
        current = self.node
        for w in word:
            if w not in current.children:
                new_node = Node()
                current.children[w] = new_node
            current = current.children[w]
        current.is_end = True
            
    def search(self, word: str) -> bool:
        current = self.node
        for w in word:
            if w in current.children:
                current = current.children[w]
            else:
                return False
        if current.is_end:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        current = self.node
        for w in prefix:
            if w in current.children:
                current = current.children[w]
            else:
                return False
        
        return True
    #

        


# Your Trie object will be instantiated and called as such: