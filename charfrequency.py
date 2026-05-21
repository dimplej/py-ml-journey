msg="banana"
freq={}
for x in msg:
    freq[x]=freq.get(x,0)+1
print(freq)
    