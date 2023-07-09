# 대칭 차집합, 1269

import sys
input = sys.stdin.readline

num_a, num_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

# set으로 하면 뺄 수 있음
print(len(a-b) + len(b-a))




