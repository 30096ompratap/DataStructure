from collections import deque

def opening(i):
    return i=="{" or i == "[" or i =="("

def closing(o,c):
    return o=="{" and c=="}" or o=="[" and c=="]" or o=="(" and c==")"
stack = deque()

s="{}{{{}}}(){}[}"
flag=True
for i in s:
    if opening(i):
        stack.append(i)
    else:
        if not stack:
            flag=False
            break
        elif closing(stack[-1],i):
            stack.pop()
        else:
            flag=False
            break
if not stack and flag:
    print("true")
else:
    print("false")
