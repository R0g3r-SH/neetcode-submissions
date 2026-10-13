class Solution:
    def isValid(self, s: str) -> bool:
        
        symbols = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        stack = []


        for char in s:

            if char in symbols:
                if stack != [] and stack[-1] == symbols[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return stack == []
        