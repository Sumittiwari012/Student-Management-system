import csv
import pandas
import json
from matplotlib import pyplot
from department import createDep

def batchCreate(bat_name):
    bat_id = bat_name[:3] + bat_name[6:8]
    dep_id = bat_id[:3]
    csv_reader = []
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == bat_id):
            print("This batch ID already exists!")
            return
    data = [bat_id, bat_name, dep_id, "", ""]
    with open("batch.csv", "a", newline = "\n") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)
    print("Enter the courses in batch: ")
    while(True):
        cour_id = input("Enter the course ID (to stop enter STOP): ")
        with open("batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        if(csv_reader[len(csv_reader) - 1][3] != ""):
            check = 0
            temp = csv_reader[len(csv_reader) - 1][3].split(":")
            for x in temp:
                if(x == cour_id):
                    print("Course is already added!")
                    check = 1
            if(check == 1):
                continue
        if(cour_id.upper() == "STOP"):
            break
        else:
            with open("course.csv", "r", newline = "\n") as f:
                csv_reader = list(csv.reader(f, delimiter=","))
            check = 0
            for i in range(0, len(csv_reader)):
                if(csv_reader[i][0] == cour_id):
                    with open("batch.csv", "r", newline = "\n") as f:
                        csv_reader = list(csv.reader(f, delimiter=","))
                    check = 1
                    if(csv_reader[len(csv_reader) - 1][3] == ""):
                        csv_reader[len(csv_reader) - 1][3] = csv_reader[len(csv_reader) - 1][3] + cour_id
                    else:
                        csv_reader[len(csv_reader) - 1][3] = csv_reader[len(csv_reader) - 1][3] + ":" + cour_id
                    df = pandas.read_csv("batch.csv")
                    df.loc[len(csv_reader) - 2, "list_of_courses"] = csv_reader[len(csv_reader) - 1][3]
                    df.to_csv("batch.csv", index = False)
            if(check == 0):
                print("This course does not exist! Please create course first.")
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == dep_id):
            check = 1
            if(csv_reader[i][2] == ""):
                csv_reader[i][2] = csv_reader[i][2] + bat_id
            else:
                csv_reader[i][2] = csv_reader[i][2] + ":" + bat_id
            df = pandas.read_csv("department.csv")
            df.loc[i-1, "list_of_batches"] = csv_reader[i][2]
            df.to_csv("department.csv", index = False)
    if(check == 0):
        print("This department does not exist.... Creating new department")
        dep_name = input("Enter name of the department: ")
        createDep(dep_id, dep_name)
        with open("department.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        csv_reader[len(csv_reader) - 1][2] = csv_reader[len(csv_reader) - 1][2] + bat_id
        df = pandas.read_csv("department.csv")
        df.loc[len(csv_reader) - 2, "list_of_batches"] = csv_reader[len(csv_reader) - 1][2]
        df.to_csv("department.csv", index = False)

def viewCourses(bat_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    courses = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == bat_id):
            check = 1
            courses = csv_reader[i][3].split(":")
            break
    if(check == 0):
        print("This batch ID does not exist!")
        return
    print("Courses in " + bat_id + ":")
    for course in courses:
        print(course)
        
def viewStudents(bat_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == bat_id):
            check = 1
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("This batch ID does not exist!")
        return
    print("Students in " + bat_id + ":")
    for student in students:
        print(student)

def viewPerformance(bat_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == bat_id):
            check = 1
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("This batch ID does not exist!")
        return
    for student in students:
        with open("student.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(student == csv_reader[i][0]):
                print("Student ID: " + student)
                print("Student Name: " + csv_reader[i][1])
                print("Student Roll Number: " + csv_reader[i][2])
        with open("course.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        all_marks = []
        for i in range(1, len(csv_reader)):
            all_marks.append(json.loads(csv_reader[i][2]))
        t_marks = 0
        divs = 0
        for subjects in all_marks:
            if(isinstance(subjects.get(student), int)):
                t_marks += subjects.get(student)
                divs += 1
        print("Percentage obtained: " + str(t_marks/divs))
        print()


def pieChart(bat_id):
    with open("batch.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    students = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == bat_id):
            check = 1
            students = csv_reader[i][4].split(":")
            break
    if(check == 0):
        print("This This batch ID does not exist!")
        return
    percentages = [">=90", ">=80", ">=70", ">=60", ">=50", "Failed"]
    num = [0, 0, 0, 0, 0, 0]
    for student in students:
        with open("course.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        all_marks = []
        for i in range(1, len(csv_reader)):
            all_marks.append(json.loads(csv_reader[i][2]))
        t_marks = 0
        divs = 0
        for subjects in all_marks:
            if(isinstance(subjects.get(student), int)):
                t_marks += subjects.get(student)
                divs += 1
        percent = t_marks/divs
        if(percent >= 90):
            num[0] += 1
        elif(percent >= 80):
            num[1] += 1
        elif(percent >= 70):
            num[2] += 1
        elif(percent >= 60):
            num[3] += 1
        elif(percent >= 50):
            num[4] += 1
        else:
            num[5] += 1
    for i in range(len(num) - 1, -1, -1):
        if(num[i] == 0):
            del num[i]
            del percentages[i]
    pyplot.pie(num, labels = percentages)
    pyplot.show()
