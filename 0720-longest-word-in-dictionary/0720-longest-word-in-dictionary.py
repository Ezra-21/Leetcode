from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        # Build Trie
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.isWord = True

        self.longest = ""

        def dfs(node, path):
            # Only continue DFS if current path is a word or empty root
            if node != root and not node.isWord:
                return
            # Update longest word
            if len(path) > len(self.longest) or (len(path) == len(self.longest) and path < self.longest):
                self.longest = path
            # DFS on children in sorted order to ensure lexicographical priority
            for ch in sorted(node.children.keys()):
                dfs(node.children[ch], path + ch)

        dfs(root, "")
        return self.longest
