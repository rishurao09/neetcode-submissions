class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")":"(","}":"{","]":"["} 
        stack = []
        for i in s : 
            if i not in pairs : 
                stack.append(i)
            else : 
                if not stack : 
                    return False 
                top = stack[-1]
                if top == pairs[i]:
                    stack.pop()
                else : 
                    return False 
        return not stack