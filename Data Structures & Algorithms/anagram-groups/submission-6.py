class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = defaultdict(list)


        for s in strs:

            cnt = [0] * 26
    
            for char in s:
                cnt[ord(char)-ord('a')] +=1

            dic[tuple(cnt)].append(s)
            
        
        return list(dic.values())