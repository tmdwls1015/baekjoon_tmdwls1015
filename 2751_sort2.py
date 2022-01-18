import sys
n = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline()) for i in range(n)]

arr.sort()
for a in arr:
	print(a)
