if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    a=0
    q=student_marks[query_name]
    for i in range(0,len(q)):
        a+=q[i]
    f=a/3
    print('%.2f' %f)