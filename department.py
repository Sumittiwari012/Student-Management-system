import json
import csv
from matplotlib import pyplot

def createDep(dep_id, dep_name):
    csv_reader = []
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == dep_id):
            print("This department ID already exists!")
            return
    data = [dep_id, dep_name, ""]
    with open("department.csv", "a", newline = "\n") as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(data)

def viewBatches(dep_id):
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    batches = []
    for i in range(0, len(csv_reader)):
        if(csv_reader[i][0] == dep_id):
            check = 1
            batches = csv_reader[i][2].split(":")
            break
    if(check == 0):
        print("This department ID does not exist!")
        return
    print("Batches in " + dep_id + ":")
    for batch in batches:
        print(batch)

def viewPerformanceD(dep_id):
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    batches = []
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == dep_id):
            check = 1
            batches = csv_reader[i][2].split(":")
            break
    if(check == 0):
        print("This department ID does not exist!")
        return
    if(len(batches) == 0):
        print("No batches in this department!")
        return
    performances = []
    for batch in batches:
        students = []
        student_performances = []
        with open("batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(csv_reader[i][0] == batch):
                students = csv_reader[i][4].split(":")
                break
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
            if(divs != 0):
                student_performances.append(t_marks/divs)
            else:
                student_performances.append(0)
        t_marks = 0
        divs = 0
        for x in student_performances:
            t_marks += x
            divs += 1
        if(divs != 0):
            performances.append(t_marks/divs)
        else:
            performances.append(0)
    t_marks = 0
    divs = 0
    for i in range(0, len(batches)):
        t_marks += performances[i]
        divs += 1
    avg_percentage = 0
    if(divs != 0):
        avg_percentage = t_marks/divs
    print("Average percentage obtained by all batches in " + dep_id + ": " + str(avg_percentage))

def linePlot(dep_id):
    with open("department.csv", "r", newline = "\n") as f:
        csv_reader = list(csv.reader(f, delimiter=","))
    check = 0
    batches = []
    for i in range(1, len(csv_reader)):
        if(csv_reader[i][0] == dep_id):
            check = 1
            batches = csv_reader[i][2].split(":")
            break
    if(check == 0):
        print("This department ID does not exist!")
        return
    if(len(batches) == 0):
        print("No batches in this department")
        return
    performances = []
    for batch in batches:
        students = []
        student_performances = []
        with open("batch.csv", "r", newline = "\n") as f:
            csv_reader = list(csv.reader(f, delimiter=","))
        for i in range(0, len(csv_reader)):
            if(csv_reader[i][0] == batch):
                students = csv_reader[i][4].split(":")
                break
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
            if(divs != 0):
                student_performances.append(t_marks/divs)
            else:
                student_performances.append(0)
        t_marks = 0
        divs = 0
        for x in student_performances:
            t_marks += x
            divs += 1
        if(divs != 0):
            performances.append(t_marks/divs)
        else:
            performances.append(0)
    pyplot.plot(batches, performances)
    pyplot.show()
