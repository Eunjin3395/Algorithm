import sys


class Stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,x):
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            top=-1
        else:
            top = self.stack.pop()
        return top
    
    def top(self):
        if not self.stack:
            return -1
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    
    def empty(self):
        return (0 if len(self.stack) else 1)
    

stack= Stack()

n=int(sys.stdin.readline())

for i in range(n):
    command = sys.stdin.readline()

    if "push" in command:
        num = int(command.split()[1])
        stack.push(num)
    
    if "pop" in command:
        result = stack.pop()
        print(result)
    
    if "top" in command:
        print(stack.top())

    if "size" in command:
        print(stack.size())

    if "empty" in command:
        print(stack.empty())
