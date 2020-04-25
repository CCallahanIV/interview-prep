import heapq
from typing import List
import re


class KeywordItem:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word < other.word
        return self.freq < other.freq


def top_k_keywords(k: int, keywords: List[str], reviews: List[str]) -> List[str]:
    keyword_count = {}
    keyword_set = set(keywords)

    heap = []

    for review in reviews:
        words = review.split()
        for word in words:
            cleaned_word = re.sub("[\W_]+", '', word).lower()
            if cleaned_word in keyword_set:
                keyword_count[cleaned_word] = keyword_count.setdefault(cleaned_word, 0) + 1
    
    for word, freq in keyword_count.items():
        heapq.heappush(heap, KeywordItem(word, freq))

    return [item.word for item in heapq.nlargest(k, heap)]
