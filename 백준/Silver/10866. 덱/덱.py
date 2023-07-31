import sys

class Dequeue:
    def __init__(self):
        self.deq = []
    
    def push_front(self,x):
        self.deq.insert(0,x)

    def push_back(self,x):
        self.deq.append(x)

    def pop_front(self):
        if self.deq:
            return self.deq.pop(0)
        else:
            return -1
    
    def pop_back(self):
        if self.deq:
            return self.deq.pop()
        else:
            return -1
        
    def size(self):
        return len(self.deq)
    
    def empty(self):
        return (0 if self.deq else 1)
    
    def front(self):
        if self.deq:
            return self.deq[0]
        else:
            return -1
        
    def back(self):
        if self.deq:
            return self.deq[-1]
        else:
            return -1
        

n = int(sys.stdin.readline())

deq=Dequeue()

for i in range(n):
    command = sys.stdin.readline().rstrip()

    if("push_front" in command):
        x = int(command.split()[1])
        deq.push_front(x)
    elif("push_back" in command):
        x = int(command.split()[1])
        deq.push_back(x)
    elif("pop_front"in command):
        print(deq.pop_front())
    elif("pop_back" in command):
        print(deq.pop_back())
    elif("size" in command):
        print(deq.size())
    elif("empty" in command):
        print(deq.empty())
    elif("front" in command):
        print(deq.front())
    elif("back" in command):
        print(deq.back())
