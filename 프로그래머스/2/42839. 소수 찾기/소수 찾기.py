from itertools import combinations, permutations
from math import *
# combination으로 가능한 모든 숫자 조합 만들기
# 그 다음 모든 숫자 조합에 대해 소수인지 판별?

def isPrime(n):
    s =set()
    for x in range(1,int(sqrt(n))+1):
        if(n%x==0):
            s.add(x)
            s.add(n//x)
    return len(s)==2
            
        

def solution(numbers):
    arr = list(numbers)
    comb_list = []
    for i in range(1,len(arr)+1):
        comb_list.extend(list(combinations(arr,i)))
    print(comb_list)
    
    s = set()
    for elem in comb_list:
        s.add(int(''.join(elem)))
        
        if(len(elem)==1):
            continue
        
        print("elem:",elem)
        
        for perm in permutations(range(0,len(elem))):
            temp =""
            for i in perm:
                temp+=elem[i]
            print(temp)
            s.add(int(temp))
    print(s) 
    
    answer = 0
    for num in s:
        if(isPrime(num)):
            print("isPrime")
            answer+=1

    return answer
