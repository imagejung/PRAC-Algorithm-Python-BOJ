# 8진수, 10진수, 16진수, 11816

import sys
x = input()

if x[0] == '0':
    if x[1] == 'x':
        print(int(x,16)) # 0x로 시작되니 16진수로 바꾸자 해도 오류안남
    else:
        print(int(x,8)) # 어차피 0은 신경안씀
else:
    print(int(x))
