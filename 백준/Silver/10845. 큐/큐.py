import sys
import queue

class Queue:
    def __init__(self):
        self.queue=[]
    
    def push(self,x):
        self.queue.append(x)

    def pop(self):
        if (self.queue):
            return self.queue.pop(0)
        else:
            return -1
    
    def size(self):
        return len(self.queue)
    
    def empty(self):
        return (0 if self.queue else 1)
    
    def front(self):
        if(self.queue):
            return self.queue[0]
        else:
            return -1
        
    def back(self):
        if(self.queue):
            return self.queue[-1]
        else:
            return -1
        

n = int(sys.stdin.readline())

q= Queue()

for i in range(n):
    command = sys.stdin.readline().rstrip()

    if("push" in command):
        x = int(command.split()[1])
        q.push(x)
    elif("pop" in command):
        print(q.pop())
    elif("size" in command):
        print(q.size())
    elif("empty" in command):
        print(q.empty())
    elif("front" in command):
        print(q.front())
    elif("back" in command):
        print(q.back())