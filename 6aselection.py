def selection(arr,n):
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
        (arr[i],arr[min])=(arr[min],arr[i])

arr = []
n = int(input())
for i in range(n):
    element = int(input(f"Enter element {i+1} :"))
    arr.append(element)
selection(arr,n)
print(arr)