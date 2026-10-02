class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_hash = {']':'[', '}':'{', ')':'('}

        for i in s:
            if i in my_hash:
                if stack and stack[-1] == my_hash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
        