import sys

stack1 = list(sys.stdin.readline().rstrip())
stack2 = []

N = int(sys.stdin.readline())

for i in range(N):
    command = sys.stdin.readline().rstrip()
    if(command == "L"):
      if(stack1):
        char = stack1.pop()
        stack2.append(char)

    elif(command =="D"):
      if(stack2):
        char = stack2.pop()
        stack1.append(char)

    elif(command =="B"):
      if(stack1):
        stack1.pop()

    else:
      x = command.split()[1]
      stack1.append(x)

stack1.extend(reversed(stack2))
print(''.join(stack1))