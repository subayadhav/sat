from itertools import combinations
u2,v=map(int,input().split())
w=len(str(u2))
x=list(combinations(str(u2),w-v))
x=(sorted(x))
y="".join(x[0])
print(y)
