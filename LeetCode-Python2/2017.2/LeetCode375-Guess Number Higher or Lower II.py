import random

n=2
sum = 0
c = 0
if n > 1:
    a = random.randint(1, n)
    b = random.randint(1, n)
    d = 1
    while b != a:
        if b > a:
            c = b
            sum += b
            if d < (b - 1):
                b = random.randint(d, b - 1)
        elif b < a:
            d = b
            sum += b
            if (b + 1) < c:
                b = random.randint(b + 1, c)
    print sum
elif n == 1:
    print 0