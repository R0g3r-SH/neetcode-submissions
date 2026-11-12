class Solution:
    def calPoints(self, operations: List[str]) -> int:

        symbols = {"+","D","C"}

        stack = []
        for val in operations:
            print(stack)

            if val in symbols and stack != []: 

                res = 0
                if val == "+":
                    v1 = stack[-2]
                    v2 = stack[-1]
                    res = int(v1) + int(v2)
                    stack.append(res)
                elif val == "D":
                    v1 = stack[-1]
                    res = int(v1)*2
                    stack.append(res)
                elif val == "C":
                    stack.pop()
            
            else:
                stack.append(int(val))

        return sum(stack)
