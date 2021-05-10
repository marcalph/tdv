# using prefix hashset
# O(n*m) time, O(n) space
def replaceWords(self, roots, sentence):
    rootset = set(roots)

    def replace(word):
        for i in xrange(1, len(word)):
            if word[:i] in rootset:
                return word[:i]
        return word

    return " ".join(map(replace, sentence.split()))

#using trie
#O(n) spacetime
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = dict()
        end = "#end"
        for word in dictionary:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur[end] = word

        splitted = sentence.split()
        for idx, word in enumerate(splitted):
            node=trie
            for letter in word:
                if letter not in node or end in node:
                    break
                node = node[letter]
            splitted[idx] = node.get(end, word)
        
        return " ".join(splitted)