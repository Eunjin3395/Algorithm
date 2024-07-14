import sys

N,M = map(int,sys.stdin.readline().split());

basket = [0]*N;
for c in range(M):
  I, J, K = map(int,sys.stdin.readline().split());
  for i in range(I-1,J):
    basket[i] = K

for elem in basket:
  print(elem,end=" ")