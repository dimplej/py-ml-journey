n,m=map(int,input().split())
array=map(int,input().split())
A=map(int,input().split())
B=map(int,input().split())
lst=list(array)
A_set=set(A)
B_set=set(B)
happiness=0
for i in lst:
    if i in A_set:
        happiness+=1
    elif i in B_set:
        happiness-=1
print(happiness)