A = [1,2,5,6,3]
A.sort()
y=max(A)
for i in range(1,y):
    if i!=A[i-1]:
        print (i)
        break

