class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = '+-*/'
        for i in tokens : 
            if i in op : 
                a = stack.pop()
                b = stack.pop()
                if i == '+':
                    res = b+a 
                elif i == '-':
                    res = b-a
                elif i == '*':
                    res = b*a
                else : 
                    res = int(b/a)
                stack.append(res)
            else : 
                stack.append(int(i))
        return stack[-1]