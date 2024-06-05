def insertion(arr,n):
    if(n<=1):
        return
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while (j>=0 and key<arr[j]):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr = []
n = int(input())
for i in range(n):
    element = int(input(f"Enter element {i+1} :"))
    arr.append(element)
insertion(arr,n)
print(arr)