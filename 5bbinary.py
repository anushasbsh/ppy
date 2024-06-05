def binary(arr,l,h,key):
    if(h>=l):
        mid = (l+h)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]>key):
            return binary(arr,l,h-1,key)
        else:
            return binary(arr,l+1,h,key)
    else:
        return -1
arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))
key = int(input())
res = binary(arr,0,n-1,key)
if(res!=-1):
    print("Found at", res)
else:
    print("Not Found")