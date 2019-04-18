students_list = []


# id 는 variable로 쓰면 안되는 건가요?
# Class는 대문자로 사용한다고 배운거 같은데, 소문자도 되는군요...  
class Student:
    def __init__(self, ID, name, birth, mid_score, final_score):
        self.ID = ID
        self.name = name
        self.birth = birth
        self.mid_score = mid_score
        self.final_score = final_score
        self.average = (int(mid_score) + int(final_score)) / 2
        self.grade = grade_calculate(self.average)
        

def grade_calculate(a):
    if a >= 90:
        return "A"
    if 90 > a >= 80:
        return "B"
    if 80 > a >= 70:
        return "C"
    if 70 > a >= 60:
        return "D"
    if 60 > a:
        return "F"


def add_a_new_entry():
    print("Register a new student on a system")
    stud_id = str(input("enter Student id: "))
    stud_name = input("enter Student name: ")
    stud_birth = input("enter Student birth(yyyy-mm-dd): ")
    mid_score = int(input("enter Student mid_score: "))
    final_score = int(input("enter Student final_score: "))
    
    student = Student(stud_id, stud_name, stud_birth, mid_score, final_score)
    students_list.append(student)

def delete_an_entry():
    print("Delete student information on system")
    search_id = input("Enter student ID or name: ")
    for Student in students_list:
        if search_id == Student.name or Student.ID:
            d_check = input("Do you really delete this one?(Y/N)").lower()
            if d_check == "y":
                students_list.remove(Student)

def find_some_item_from_entry():
    print("View your average score and grade")
    search_id = input("Enter student ID or name: ")
    for Student in students_list:
        if search_id == Student.name or Student.ID:
            print("Your average score is ", Student.average, "and grade is ", Student.grade)
        else:
            break

def modify_an_entry():
    print("Change score")
    search_id = input("Enter student ID or name: ")
    for Student in students_list:
        if search_id == Student.name or Student.ID:
            select = input("Which score do you want to change?(mid_term: m, final: f)").lower()
            if select == "m":
                new_mid_score = input("Enter new score: ")
                Student.mid_score = new_mid_score
                print("Mid_term score is changed to "+Student.mid_score)
            elif select =="f":
                new_final_score = input("Enter new score: ")
                Student.final_score = new_final_score
                print("Final score is changed to "+Student.final_score)
                

def read_personal_data_from_a_file():
    file = input("file name: ")
    with open(file) as f:
        while True:
            read_data = f.readline()
            if not read_data:
                break
            x = read_data.split("\t")
            
            student = Student(x[1],x[2],x[3],x[4],x[5].rstrip())
            students_list.append(student)
            
            
def print_all_entries():
    for i, student in enumerate(students_list):
        print(i+1, student.ID, student.name, student.birth, student.mid_score, student.final_score, student.average, student.grade)
        
def sort_entries():
    sort_std = input("Sort by n:name, a:average_score, g: grade: ")
    if sort_std == "n":
        students_list.sort(key=lambda std: std.name, reverse=False)
        print_all_entries()
    elif sort_std == "a":
        students_list.sort(key=lambda std: std.average, reverse=True)
        print_all_entries()
    elif sort_std == "g":
        students_list.sort(key=lambda std : std.grade, reverse=True)
        print_all_entries()
        
def write_the_contents():
    file = input("file name: ")
    with open(file,'w') as f:
        for i, student in enumerate(students_list):
            data = str(i+1)+"\t"+str(student.ID)+"\t"+str(student.name)+"\t"+str(student.birth)+"\t"+str(student.mid_score)+"\t"+str(student.final_score)+"\t"+str(student.average)+"\t"+str(student.grade)+"\n"
            f.write(data)
    f.close()
   

while True:
    print(" a: add a new entry\n"
          ,"d: delete an entry\n"
          ,"f: find some item from entry\n"
          ,"m: modify an entry\n"
          ,"p: print the contents of all entries\n"
          ,"r: read personal data from a file\n"
          ,"s: sort entries\n"
          ,"q: quit\n"
          ,"w: write the contents to the same files")
    command = input("Choose one of the options above:").lower() # below로 하고싶었는데 못했음...그래서 above로..
    
    if command == "a":
        add_a_new_entry()
    
        
    elif command == "d":
        delete_an_entry()

    elif command == "f":
        find_some_item_from_entry()
        
    elif command == "m":
        modify_an_entry()
        
    elif command == "p":
        print_the_content_of_all_entries()
        
    elif command == "r":
        read_personal_data_from_a_file()
        
    elif command == "s":
        sort_entries()    
        
    elif command == "w":
        write_the_contents()
        
    elif command == "q":
        break

   


    