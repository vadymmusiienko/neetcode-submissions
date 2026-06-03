class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    second, first = stack.pop(), stack.pop()
                    stack.append(first - second)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    second, first = stack.pop(), stack.pop()
                    stack.append(int(first / second))
                case _:
                    stack.append(int(token))
        
        assert(len(stack) == 1)
        return stack[0]

        