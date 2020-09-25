n = input()
sum = 0
number = n.split()
arr = list(map(int, number))
for i in range(len(arr)):
    m = int(arr[i])
    sum += m
print(sum)