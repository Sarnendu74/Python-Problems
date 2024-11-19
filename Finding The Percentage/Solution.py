if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if query_name in student_marks:
        marks = [x[1] for x in student_marks.items() if x[0]==query_name][0]
        average = sum(marks)/len(marks)
        print(f'{average:.2f}')
    else:
        pass
            