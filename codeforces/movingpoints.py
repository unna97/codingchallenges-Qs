'''
Author : Unnati Patel
Language : Python
URL : https://codeforces.com/problemset/problem/1311/F
'''

from collections import orderedDict
n = int(input())
X = map(int, input().split())
V = map(int, input().split())
A = dict(zip(X,V))
A = SortedDict(A)
print(A)
