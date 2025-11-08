class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            elif c in ')]}':
                if len(stack) == 0:
                    return False
                top = stack[-1]
                if (c == ')' and top == '(') or ( c == ']' and top == '[') or (c == '}' and top == '{'):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
                

        
        