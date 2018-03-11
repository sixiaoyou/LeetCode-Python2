
A="abcde"
B="cdeab"
for i in range(len(A)):
    s = A[i + 1:] + A[:i+1]
    print s
    if s== B:
        print True
print False
