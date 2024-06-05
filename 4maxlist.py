list = []
n = int(input())
for i in range(1,n+1):
    e = int(input("Enter element {}".format(i)))
    list.append(e)
list.sort(reverse = True)
print(list[:1])