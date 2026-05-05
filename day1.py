if __name__ == '__main__':
    n = int(input().strip())
if n%2!=0:
    print("Weird")
else:
    if 2<=n<=5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(float(a/b))


n = int(input())
for i in range(0,n):
    print(i*i)

def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
year = int(input())
print(is_leap(year))


 n = int(input())
    for i in range(1,n+1):
        print(i,end="")


x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i, j, k] 
          for i in range(x + 1) 
          for j in range(y + 1) 
          for k in range(z + 1) 
          if i + j + k != n]
print(result)


n = int(input())
    arr = map(int, input().split())
    x=list(set(arr))
    x.sort()
    print(x[-2])


students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    x=sorted(set([student[1] for student in students]))
    res=x[1]
    names=[student[0] for student in students if student[1]==res]
    names.sort()
    for name in names:
        print(name) 


n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    marks_list=student_marks[query_name]  
    res=sum(marks_list)/len(marks_list)
    print(f"{res:.2f}")




