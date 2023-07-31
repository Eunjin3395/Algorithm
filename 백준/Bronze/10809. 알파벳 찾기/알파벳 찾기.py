import sys

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

string = sys.stdin.readline().rstrip()

for elem in alphabet:
    if(elem == 'z'):
        print(string.find(elem),end="")
    else:
        print(string.find(elem),end=" ")