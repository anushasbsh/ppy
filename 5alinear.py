def linear(arr,n,key):
    for i in range(n):
        if (arr[i]==key):
            return i
    return -1
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
key = int(input())
res = linear(arr,n,key)
if(res!=-1):
    print("Found at :",res)
else:
    print("Not found")
