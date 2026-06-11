from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            alph = [0]*26
            for w in word:
                alph[ord(w)-ord("a")]+=1
            res[tuple(alph)].append(word)
        return list(res.values())
