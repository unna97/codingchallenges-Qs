'''
Author : Unnati Patel
Language : Python
Algorithm : Insertion Sort
'''

def swap(a,i,j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def should_swap(a,b):
    return(a > b)

w = input()
A = list(map(int,input().split()))
for key in range(1,len(A)):
    for i in range(key,0,-1):
        if should_swap(A[i - 1],A[i]):
            swap(A,i - 1,i)
print(*A,sep = " ")

'''
    if computational_cost(compare) >> computational_cost(swaps) --> binary search help
    binary Insertionsort
'''
