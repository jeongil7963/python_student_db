from itertools import count
import sys

studentList = []
_ids = 0


class Student:

    def __init__(self, id_, name_, birth_, mid_score_, last_score_):
        global _ids
        _ids += 1

        self.idx = _ids
        self.id = id_
        self.name = name_
        self.birth = birth_
        self.mid_score = mid_score_
        self.last_score = last_score_
        self.average = ( float(mid_score_) + float(last_score_))/2
        self.grade = calculate_grade(self.average)

    def print(self):
        print(str(self.idx) + ", " + self.id + ", " + self.name + ", " +
              self.birth + ", " + self.mid_score + ", " + self.last_score +
              ", " + str(self.average) + ", " + self.grade)


def calculate_grade(average):
    if average > 90:
        return "A"
    elif 90 >= average and average > 80:
        return "B"
    elif 80 >= average and average > 70:
        return "C"
    elif 70 >= average and average > 60:
        return "D"
    elif 60 >= average:
        return "F"

def add_a_new_entry():
    print("Start adding a new entry")
    input_id = input("Enter student id : ")
    input_name = input("Enter student name : ")
    input_birth = input("Enter student birth : ")
    input_mid_score = input("Enter student mid score : ")
    input_final_score = input("Enter student final score : ")

    student_object = Student(input_id, input_name, input_birth, input_mid_score, input_final_score)
    studentList.append(student_object)

def delete_an_entry():
    print("Start modifying an entry")
    id_or_name_val = input("Enter Student Id or Name : ")
    idx = 0

    for student in studentList:
        if student.name == id_or_name_val:
            idx = student.idx

        elif student.id == id_or_name_val:
            idx = student.idx

    if idx == 0:
        print("Input Value Error")
        return
    else:
        studentList.pop(idx-1)
        for num in range(idx-1, len(studentList)):
            studentList[num].idx = num+1

    global _ids
    _ids -= 1


def find_some_item_from_entry():
    print("Start find some item from entry")
    id_or_name_val = input("Enter Student Id or Name : ")
    idx = 0

    for student in studentList:
        if student.name == id_or_name_val:
            idx = student.idx

        elif student.id == id_or_name_val:
            idx = student.idx

    if idx == 0:
        print("No matching values found.")
    else:
        print("Print the average score and grade of a student")
        print("Average score : ", studentList[idx - 1].average)
        print("Grade : ", studentList[idx - 1].grade)


def modify_an_entry():
    print("Start modifying an entry")
    id_or_name_val = input("Enter Student Id or Name : ")
    idx = 0

    for student in studentList:
        if student.name == id_or_name_val:
            idx = student.idx

        elif student.id == id_or_name_val:
            idx = student.idx

    if idx == 0:
        print("No matching values found.")
    else:
        print("Choose the midterm and final exam you want to correct")
        input_val = input("Enter mid or final : ")

        print("Student idx : ", idx)
        if input_val == "mid":
            input_mid_score_val = input("Enter mid score to modify : ")
            studentList[idx - 1].mid_score = input_mid_score_val
        elif input_val == "final":
            input_final_score_val = input("Enter final score to modify : ")
            studentList[idx - 1].final_score = input_final_score_val
        else:
            print("Input Value Error")
            return

    print("Please check the modified details")
    studentList[idx - 1].print()


def print_the_contents_of_all_entries():
    print("Start printing the contents of all entries")
    for student in studentList:
        student.print()


def read_personal_data_from_a_file():
    print("Start reading personal data from a file")
    file_data = input("enter the file name : ")
    try:
        data = open(file_data)

        for each_line in data:
            try:
                student_val = each_line.split("\t")
                student_val[5] = student_val[5][:-1]
                student_object = Student(student_val[1], student_val[2], student_val[3], student_val[4], student_val[5])
                studentList.append(student_object)
            except ValueError:
                pass

        data.close()
    except IOError:
        print('The datafile is missing!')


def sort_entries():
    print("Start sorting entries")
    print("Choose by name(n), average(a), and grade(g)")

    input_val = input("Enter n or a or g")

    if input_val == "n":
        studentList.sort( key = lambda object:object.name, reverse=True)

    elif input_val == "a":
        studentList.sort( key = lambda object:object.average, reverse=True)

    elif input_val == "g":
        studentList.sort( key = lambda object:object.grade, reverse=True)

    else:
        print("Input Value Error")
        return

    print("Please check the modified details")
    print_the_contents_of_all_entries()
    studentList.sort( key = lambda object:object.idx, reverse=True)


def quit():
    print("Start quitting the program")
    return False


def write_the_contents_to_the_same_file():
    print("Start writing the contents to the same file")
    output_val = input("Enter file name to save : ")

    try:
        write_file = open(output_val, "w")

        for student in studentList:
            write_file.write(str(student.idx) + "\t" + str(student.id) + "\t" +
                                student.name + "\t" + student.birth + "\t" +
                                str(student.mid_score) + "\t" + str(student.last_score) + "\n")

        write_file.close
    except:
        print("Unexpected Error : ", sys.exc_info())


def db_start():
    print("Start student Database Program")
    flag_quit = True

    while flag_quit:
        input_val = input("Choose one of the options below : ")
        input_val = input_val.lower()

        if input_val == 'a':
            add_a_new_entry()

        elif input_val == 'd':
            delete_an_entry()

        elif input_val == 'f':
            find_some_item_from_entry()

        elif input_val == 'm':
            modify_an_entry()

        elif input_val == 'p':
            print_the_contents_of_all_entries()

        elif input_val == 'r':
            read_personal_data_from_a_file()

        elif input_val == 's':
            sort_entries()

        elif input_val == 'q':
            flag_quit = quit()

        elif input_val == 'w':
            write_the_contents_to_the_same_file()

        else:
            print("Input Value Error")


if __name__ == '__main__':
    db_start()