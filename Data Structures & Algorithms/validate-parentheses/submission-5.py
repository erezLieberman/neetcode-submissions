class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {}
        pairs['('] = ')'
        pairs['{'] = '}'
        pairs['['] = ']'
    
        stack = []

        for c in s:
            if c in pairs.keys():
                stack.append(c)
            else:
                if stack and c == pairs[stack[len(stack)-1]]:
                    stack.pop()
                else:
                    return False
        
        if stack:
            return False
        return True