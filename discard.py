n=int(input())
numbers=set(map(int,input().split()))
commands=int(input())
for i in range(commands):
    command=input().lower().split()
    if command[0]=="pop" :
        numbers.pop()
    elif command[0]=="remove":
        sec=int(command[1])
        if sec in numbers :
            numbers.remove(sec)
    elif command[0]=="discard":
        sec=int(command[1])
        if sec in numbers :
            numbers.discard(sec)
    else:
        pass
print(sum(numbers))