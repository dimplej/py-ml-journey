m=input()

a = set(map(int, input().split()))

n=input()

b = set(map(int, input().split()))

print(*sorted(a ^ b), sep="\n")