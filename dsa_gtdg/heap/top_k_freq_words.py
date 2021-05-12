class FreqWord(object):
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq != other.freq:
            return lt(self.freq, other.freq) # self.freq < other.freq
        else:
            # opposite sort
            return lt(other.word, self.word) # other.word < self.word

#O(N log k) | O(n) but slower because of custom code in __lt__
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        words_with_count = collections.Counter(words)
            
        min_heap = list()
        for word, count in words_with_count.items():
            heapq.heappush(min_heap, FreqWord(count, word))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [heapq.heappop(min_heap).word for _ in range(k)][::-1] 



# O(nlogn)
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = collections.Counter(words)
        return sorted(cnt, key= lambda x: (-cnt[x], x))[:k] 