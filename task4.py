def calculate_average_grades():
    grades = []
    while True:
        grade = input("Enter a grade (-1 to stop): ")
        if grade == '-1':
            break
        grades.append(int(grade))

    average_grade = sum(grades) / len(grades)
    print(int(average_grade))
    for grade in grades:
        print(grade)

if __name__ == "__main__":
    calculate_average_grades()
