class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "*", "-", "/"]
        for num in tokens:
            if num in operations:
                b = stack.pop()
                a = stack.pop()
                #if a in operations or b in operations:
                #    return None
                if num == "+":
                    stack.append(a+b)
                elif num == "-":
                    stack.append(a-b)
                elif num == "*":
                    stack.append(a*b)
                elif num == "/":
                    stack.append(int(float(a)/b))
            else:
                stack.append(int(num))
        return stack.pop()

            