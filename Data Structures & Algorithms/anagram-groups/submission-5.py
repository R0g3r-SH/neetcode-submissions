class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
      res = defaultdict(list)

      for s in strs:

        cnt = [0]*26

        for char in s :
            cnt[ord(char)-ord("a")]+=1
        res[tuple(cnt)].append(s)
      return list(res.values())



 