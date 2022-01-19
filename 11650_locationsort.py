n=int(input())
arr=[]
for i in range(n):
	tmp = list(map(int, input().split()))
	arr.append(tmp)
for i in sorted(arr):
	print(i[0],i[1])