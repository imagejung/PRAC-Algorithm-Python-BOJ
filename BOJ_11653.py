# 소인수분해, 11653

n = int(input())
i = 2

while n!=1:
    if n % i == 0:
        print(i)
        n/=i
    else:
        i+=1

정