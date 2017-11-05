'''
LeetCode 400:Nth Digit
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3
Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
n1=0
if 0<n<10:
    finalNumber=n
else:
    for i in xrange(10):
        n1+=9*10**i*(i+1)
        n2=n1+9*10**(i+1)*(i+2)
        j=i
        if n1<=n<=n2:
            break
    if (n-n1)%(j+2)==0:
        number=(n-n1)/(j+2)+10**(j+1)-1
        strNumber=str(number)
        index=(n-n1-1)%(j+2)
        finalNumber=int(strNumber[index])
    else:
        number=(n-n1)/(j+2)+10**(j+1)
        strNumber=str(number)
        index=(n-n1-1)%(j+2)
        finalNumber=int(strNumber[index])
print finalNumber