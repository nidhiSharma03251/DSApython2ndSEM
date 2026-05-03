def precedence(op):
    if op == '^' or op == '$':
        return 3
    if op == '*' or op == '/':
        return 2
    if op == '+' or op == '-':
        return 1
    return 0

def infixToPrefix(infix):
    stack = []
    prefix = []
    infix = infix[::-1]
    
    for char in infix:
        if char.isalnum():
            prefix.append(char)
        elif char == ')':
            stack.append(char)
        elif char == '(':
            while stack and stack[-1] != ')':
                prefix.append(stack.pop())
            stack.pop()  
        else:  
            while (stack and precedence(char) <= precedence(stack[-1])):
                prefix.append(stack.pop())
            stack.append(char)
    
    while stack:
        prefix.append(stack.pop())
    
    return prefix[::-1]

def pop(self):
        if self.top < 0:
            print("Stack is empty")
        else:
            val = self.stk[self.top]
            self.top -= 1
            return val

# Example usage
infix_expr = "5+(10-2)*3"        
prefix_expr = infixToPrefix(infix_expr)
print("Infix Expression: ", infix_expr)


print("Prefix Expression: ", prefix_expr)
