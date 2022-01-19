import sys
n = int(sys.stdin.readline().rstrip())
cnt_arr=[0 for i in range(10001)]
for i in range(n):
	tmp = int(sys.stdin.readline())
	cnt_arr[tmp]+=1
for i in range(1,len(cnt_arr)):
	for j in range(cnt_arr[i]):
		print(i)