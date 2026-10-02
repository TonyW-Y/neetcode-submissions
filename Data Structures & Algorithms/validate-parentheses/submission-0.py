class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_hash = {')':'(', ']':'[', '}':'{'}

        for i in s:
            if i in para_hash:
                if stack and stack[-1] == para_hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
        