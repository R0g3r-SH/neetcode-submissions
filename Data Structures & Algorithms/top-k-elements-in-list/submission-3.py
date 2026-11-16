class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frec = [[] for _ in range(len(nums)+1)]

        cnt = Counter(nums)

        for num,f  in cnt.items():
            frec[f].append(num)

        res = []


        for i in range(len(frec) -1,-1,-1):
            
            fr = frec[i]

            if fr != []:
                for num in fr:
                    if len(res) == k :
                        return res
                    res.append(num)


        return res
                    



