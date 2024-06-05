import sys
list = ["a","b","c"]
print(*list,sep="\n")
tw = sum(len(s.split()) for s in list)
print(tw,"\n")
list.sort()
print(*list,sep="\n")