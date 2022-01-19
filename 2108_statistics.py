import sys

n = int(sys.stdin.readline().rstrip())

arr=[]
cnt_arr = [0 for i in range(8001)]

for i in range(n):
	tmp = int(sys.stdin.readline())
	arr.append(tmp)
	cnt_arr[tmp+4000]+=1

arr.sort()
print(round(sum(arr)/len(arr)))
print(arr[n//2])

most_freq = max(cnt_arr)
if cnt_arr.count(most_freq)==1:
	print(cnt_arr.index(most_freq)-4000)
else:
	cnt=0
	for i in range(len(cnt_arr)):
		if cnt_arr[i]==most_freq:
			cnt+=1
		if cnt==2:
			print(i-4000)
			break

print(max(arr)-min(arr))