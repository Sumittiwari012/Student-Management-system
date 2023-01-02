import csv
import json
import pandas
from matplotlib import pyplot

def enterMarks(cour_id):
    csv_reader = []
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    cour_name = ""
    stud_marks = {}
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == cour_id):
            check = 1
            cour_name = csv_reader[i][1]
            stud_marks = json.loads(csv_reader[i][2])
            break
    if(check == 0):
        print("This course ID does not exist!")
        return
    student_ids = list(stud_marks.keys())
    print("Course name: " + cour_name)
    for student in student_ids:
        marks = int(input("Enter marks obtained by " + student + ": "))
        stud_marks[student] = marks
    df = pandas.read_csv("course.csv")
    df.loc[i - 1, "marks_obtained"] = json.dumps(stud_marks)
    df.to_csv("course.csv", index = False)

def viewPerformanceE(cour_id):
    csv_reader = []
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    stud_marks = {}
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][1] == cour_id):
            check = 1
            stud_marks = json.loads(csv_reader[i][2])
            break
    if(check == 0):
        print("This course ID does not exist!")
        return
    student_ids = list(stud_marks.keys())
    for student in student_ids:
        marks = stud_marks[student]
        print("Marks obtained by " + str(marks))

def scatterPlot():
    csv_reader = []
    with open("course.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    all_marks = []
    for i in range(1, len(csv_reader)):
        all_marks.append(json.loads(csv_reader[i][2]))
    batches = []
    students = []
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        batches.append(csv_reader[i][0])
        students.append(csv_reader[i][4].split(":"))
    for course in all_marks:
        batch_performances = []
        batchesX = []
        for i in range(0, len(batches)):
            t_marks = 0
            divs = 0
            check = 0
            for student in students[i]:
                if(student == students[i][0]):
                    if(not isinstance(course.get(student), int)):
                        check = 1
                        break
                t_marks += course.get(student)
                divs += 1
            if(check == 1):
                continue
            else:
                batchesX.append(batches[i])
                batch_performances.append(t_marks/divs)
        pyplot.scatter(batchesX, batch_performances)
    pyplot.show()
