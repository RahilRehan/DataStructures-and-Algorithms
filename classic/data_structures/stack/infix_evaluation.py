def get_postfix(s):
    stack = []
    postfix = []
    for c in s:
        if c.isalnum():
            postfix.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) and stack[-1]!='(':
                e = stack.pop()
                postfix.append(e)
            stack.pop()
        elif c == '+' or c == '-':
            while len(stack) and (stack[-1] == '+' or stack[-1] == '-'):
                e = stack.pop()
                postfix.append(e)
            stack.append(c)
        else:
            continue
    while len(stack):
        e = stack.pop()
        postfix+=e
    
    return postfix

def calculate(s):
    s = s.split()
    for i, e in enumerate(s):
        if not e.isalnum():
            s = s[:i] + list(e) + s[i+1:]                
    postfix = get_postfix(s)
    stack = []
    for c in postfix:
        if c.isalnum():
            stack.append(c)
        else:
            b = int(stack.pop())
            a = int(stack.pop())
            if c == '+':
                r = a + b
            else:
                r = a-b
            stack.append(r)
    return stack[-1]

print(calculate("(1+(4+5+2)-3)+(6+8)"))