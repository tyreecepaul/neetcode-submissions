"""
return all strings that can be generated using n pairs of parentheses

count: "(", ")"

res = []
string = []
numLeft, numRight = n, n

def dfs():


dfs(numLeft, numRight)

return res

dfs(string)
- base
    if not numLeft and not numRight:
        res.append("".join(string))
        return 
- recursive case
    (check if numLeft), then add "(" to string and decrement
    dfs(string)
    (check if numRight), then add ")" to string and decrement
    dfs(string)
    
    pop ")" from string and increment
    pop "(" from string and increment

"(": 3
")": 3

string = ((()))

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(string, numLeft, numRight):
            if not numLeft and not numRight:    # base
                temp = "".join(string)
                res.append(temp)
                return

            if numLeft > 0:
                string.append("(")
                dfs(string, numLeft - 1, numRight)
                string.pop()

            if numRight > numLeft:
                string.append(")")
                dfs(string, numLeft, numRight - 1)
                string.pop()
                
        dfs([], n, n)

        return res
