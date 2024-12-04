
class Solution:
    def isValid(self, s: str) -> bool:
        stack_a = []
        for bracket in list(s):
            if bracket == ')':
                if '(' not in stack_a:
                    return False
                elif stack_a[-1] == '(':
                    stack_a.pop()
                    
            elif bracket == ']':
                if '[' not in stack_a:
                    return False
                elif stack_a[-1] == '[':
                    stack_a.pop()

            elif bracket == '}':
                if '{' not in stack_a:
                    return False
                elif stack_a[-1] == '{':
                    stack_a.pop()
            else:
                stack_a.append(bracket)
        return stack_a == []


if __name__ == '__main__':
    brakets_string = '([)]'
    brackets_output = Solution().isValid(brakets_string)

"""
    Input: brakets_string = '([)]'
    Output: False
    
"""






