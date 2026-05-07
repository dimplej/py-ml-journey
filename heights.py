def average(array):
    S = set(array)
    t = sum(S)
    l = len(S)
    r = round((t / l), 3)
    return r
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)