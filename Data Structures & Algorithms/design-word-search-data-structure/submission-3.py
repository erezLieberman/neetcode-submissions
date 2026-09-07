class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.is_word = True
            

    def search(self, word: str) -> bool:
        def dfs(node, index):
            if index == len(word):
                return node.is_word

            if word[index] == '.':
                for child_node in node.children.values():
                    if dfs(child_node, index+1):
                        return True
                return False
            else:
                if word[index] not in node.children:
                    return False

                return dfs(node.children[word[index]], index+1)
            
        return dfs(self.root, 0)
             
        
