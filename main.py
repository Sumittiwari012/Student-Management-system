while(True):
    print("Press 1 to do student operations")
    print("Press 2 to do course operations")
    print("Press 3 to do batch operations")
    print("Press 4 to do department operations")
    print("Press 5 to do examination operations")
    print("Press 0 to stop")
    x = int(input("Enter your choice: "))
    if(x == 0):
        break
    elif(x == 1):
        from student import *
        while(True):
            print("Press 1 to create a student")
            print("Press 2 to update a student's details")
            print("Press 3 to remove a student")
            print("Press 4 to generate report card of a student")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                stud_id = input("Enter the student ID: ")
                stud_name = input("Enter the student name: ")
                createStud(stud_id, stud_name)
            elif(y == 2):
                ostudent_id = input("Enter the old student ID: ")
                updateStudent(ostudent_id)
            elif(y == 3):
                stud_id = input("Enter the student ID: ")
                removeStud(stud_id)
            elif(y == 4):
                stud_id = input("Enter the student ID: ")
                reportCard(stud_id)
            else:
                print("Invalid input! Try again.")  
    elif(x == 2):
        from course import *
        while(True):
            print("Press 1 to create a course")
            print("Press 2 to view the performance of students on course")
            print("Press 3 to show the course statistics as histogram")
            print("Press 0 to return to the main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                cour_id = input("Enter the course ID: ")
                course_name = input("Enter the course name: ")
                courseCreate(cour_id, course_name)
            elif(y == 2):
                cour_id = input("Enter the course ID: ")
                checkPerformance(cour_id)
            elif(y == 3):
                cour_id = input("Enter the course ID: ")
                courseStatistics(cour_id)
            else:
                print("Invalid input! Try again.")
    elif(x == 3):
        from batch import *
        while(True):
            print("Press 1 to create a batch")
            print("Press 2 to view all the students in a batch")
            print("Press 3 to show all the courses in a batch")
            print("Press 4 to view the performance of all students in a batch")
            print("Press 5 to view the pie chart of percentage all students in a batch")
            print("Press 0 to return to the main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                bat_name = input("Enter the batch name: ")
                batchCreate(bat_name)
            elif(y == 2):
                bat_id = input("Enter the batch ID: ")
                viewStudents(bat_id)
            elif(y == 3):
                bat_id = input("Enter the batch ID: ")
                viewCourses(bat_id)
            elif(y == 4):
                bat_id = input("Enter the batch ID: ")
                viewPerformance(bat_id)
            elif(y == 5):
                bat_id = input("Enter the batch ID: ")
                pieChart(bat_id)
            else:
                print("Invalid input! Try again.")
    elif(x == 4):
        from department import *
        while(True):
            print("Press 1 to create a department")
            print("Press 2 to view all the batches in a department")
            print("Press 3 to view the average performance of all betches in a department")
            print("Press 4 to view the line plot of department statistics")
            print("Press 0 to return to the main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                dep_id = input("Enter the department ID: ")
                dep_name = input("Enter the department name: ")
                createDep(dep_id, dep_name)
            elif(y == 2):
                dep_id = input("Enter the department ID: ")
                viewBatches(dep_id)
            elif(y == 3):
                dep_id = input("Enter the department ID: ")
                viewPerformanceD(dep_id)
            elif(y == 4):
                dep_id = input("Enter the department ID: ")
                linePlot(dep_id)
            else:
                print("Invalid input! Try again.")
    elif(x == 5):
        from examination import *
        while(True):
            print("Press 1 to enter marks of all students for an exam")
            print("Press 2 to view performance of all students in an exam")
            print("Press 3 to show examination statistics as a scatter plot")
            print("Press 0 to return to main menu")
            y = int(input("Enter your choice: "))
            if(y == 0):
                break
            elif(y == 1):
                cour_id = input("Enter the course ID: ")
                enterMarks(cour_id)
            elif(y == 2):
                cour_id = input("Enter the course ID: ")
                viewPerformanceE(cour_id)
            elif(y == 3):
                scatterPlot()
            else:
                print("Invalid input! Try again.")
    else:
        print("Invalid input! Try again.")
