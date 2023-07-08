# 숫자의 합, 8595

n = int(input())
a = input()
ans = 0

num = ''
for i in a:
    if '0' <= i and i <= '9':
        num += i
    elif num != '':
        ans += int(num)
        num = ''
if num != '':
    ans += int(num)

print(ans)
