class Solution:
    def isValid(self, s: str) -> bool:
       
        opening = ['(', '{', '[']
        closing = [')', '}', ']']
    
        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            else:
                index = closing.index(c)
                if stack and stack[len(stack)-1] == opening[index]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True