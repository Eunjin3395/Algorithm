import sys

A,B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())

b = (B+C) % 60
a = (A + (B+C)//60)% 24 
print(a, b)