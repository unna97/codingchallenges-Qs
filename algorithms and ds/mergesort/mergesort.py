def Merge(A,l,r):
    k = 0
    i = 0
    j = l
    while k < l + r:
        if i < l && A[i] < A[j]:
            A[k] = A[i]
            i = i + 1
        if j < r && A[j] < A[]
