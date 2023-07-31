import sys

string = sys.stdin.readline().rstrip()

array=[]

i=0
while(i<len(string)):
    array.append(string[i:len(string)])
    i+=1

array.sort()

for elem in array:
    print(elem)