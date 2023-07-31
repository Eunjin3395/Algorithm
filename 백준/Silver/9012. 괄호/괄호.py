import sys

# ( -> push
# ) -> pop
class Stack:
    def __init__(self):
        self.stack=[]
        self.isVPS=True

    def push(self):
        self.stack.append(1)


    def pop(self):
        if self.stack: # stack에 요소 남아 있는 경우
            self.stack.pop()
        else: # stack이 비었는데 pop하려는 경우 VPS가 아님
            self.isVPS=False

    def isValid(self):
        if self.stack: # 모든 인덱스 돌고도 stack에 요소 남아 있는 경우 VPS가 아님
            self.isVPS=False
        
        return self.isVPS



n = int(sys.stdin.readline())

for i in range(n):
    string=sys.stdin.readline()

    stack = Stack()

    for k in range(len(string)):
        if(string[k]=="("):
            stack.push()
        elif(string[k]==")"):
            stack.pop()
    
    isVPS=stack.isValid()
    if(isVPS):
        print("YES")
    else:
        print("NO")

