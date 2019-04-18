# 2019451121 조규형

# coding: utf-8


student_list = []



class student:
    
    def __init__(self,ID,name,birthday,mid_score,final_score):
        
        self.ID  = str(ID)
        self.name = name
        self.birthday = str(birthday)
        self.mid_score = str(mid_score)
        self.final_score = str(final_score)
        self.average = (int(mid_score)+int(final_score))/2
        self.grade = grader(self.average)
    
    def refresh(self):

        self.average = (int(self.mid_score)+int(self.final_score))/2
        self.grade = grader(self.average)
    



def add_entry(ID,name,birthday,mid_score,final_score):
    student_list.append(student(ID,name,birthday,mid_score,final_score.rstrip()))



def del_entry(finder):
    remove_list = []
    if(len(str(finder)))==8 :
       for student in student_list:
           if student.ID == str(finder):
                remove_list.append(student)
    else :
        for student in student_list:
            print(student.name)
            if student.name == str(finder):
                remove_list.append(student)
    for student in remove_list:
        student_list.remove(student)



def grader(points):
    if points > 90:
        return "A"
    elif points > 80:
        return "B"
    else:
        return "C"



def find_entry(finder):
    if(len(str(finder)))==8 :
       for student in student_list:
           if student.ID == str(finder):
               print(finder+"의 성적은 :"+str(student.average)+" "+str(student.grade))
    else :
        for student in student_list:
           if student.name == str(finder):
               print(finder+"의 성적은 :"+str(student.average)+" "+str(student.grade))



def modify_entry(finder,flag,score):
    if(len(str(finder)))==8 :
       for student in student_list:
           if student.ID == str(finder):
                if flag == 1:
                    student.mid_score = score
                    student.refresh()
                    print(student.name+"의 중간고사 점수는  : " + str(student.mid_score))
                else:
                    student.final_score = score
                    student.refresh()
                    print(student.name+"의 기말고사 점수는  : " + str(student.final_score))
    else :
        for student in student_list:
           if student.name == str(finder):
                if flag == 1:
                    student.mid_score = score
                    student.refresh()
                    print(student.name+"의 중간고사 점수는  : " + str(student.mid_score))
                else:
                    student.final_score = score
                    student.refresh()
                    print(student.name+"의 기말고사 점수는  : " + str(student.final_score))



def print_all():
    for index, student in enumerate(student_list):
        print(index + 1, student.ID, student.name, student.birthday, student.mid_score, student.final_score, student.average, student.grade)
        



def read_data(path):
    f = open(path, 'r')
    while True:
        line = f.readline()
        if not line: break
        print(line)
        add_entry(line.split("\t")[1],line.split("\t")[2],line.split("\t")[3],line.split("\t")[4],line.split("\t")[5])
    f.close()



def sort_entry(key):
    if key == "n":
        student_list.sort(key=lambda x: x.name, reverse=True)
        print_all()
    elif key == "a":
        student_list.sort(key=lambda x: x.average, reverse=True)
        print_all()
    elif key == "g":
        student_list.sort(key=lambda x: x.grade, reverse=True)
        student_list.sort(key=lambda x: x.average, reverse=True)
        print_all()



def write_data(path):
    file = open(path, "w") 
    file.write("일련번호"+"\t"+"학생 id"+"\t"+"이름"+"\t"+"생년월일"+"\t"+"중간고사"+"\t"+"기말고사"+"\t"+"평균"+"\t"+"Grade"+"\n")
    for index,student in enumerate(student_list):
        data = str(index+1)+"\t"+str(student.ID)+"\t"+str(student.name)+"\t"+str(student.birthday)+"\t"+str(student.mid_score)+"\t"+str(student.final_score)+"\t"+ str(student.average)+"\t"+str(student.grade)+"\n"
        print(data)
        file.write(data)
    file.close() 



while True:
    command = input("Choose one of the options below: ").lower()
    if command == "q":
        break
    elif command == "a":
        input_all = input("ID, 이름, 생년월일, 중간고사, 기말고사 점수를 기입해주세요 \n 예: 20191401 권길동 2000-3-15 82 91 (스페이스 빈칸 하나가 구분자 입니다)")
        add_entry(input_all.split(" ")[0],input_all.split(" ")[1],input_all.split(" ")[2],input_all.split(" ")[3],input_all.split(" ")[4])
        print_all()
    elif command == "d":
        input_del = input("ID 나 이름을 입력하세요")
        del_entry(input_del)
        print_all()
    elif command =="f":
        find_entry(input("ID 나 이름을 입력하세요"))
    elif command =="m":
        finder = input("변경할 대상의 ID 나 이름은?")
        flag = input("중간고사 점수 변경은 1번 기말고사 변경은 0번을 눌러주세요 :")
        score = input("몇점으로 변경할까요? :")
        modify_entry(finder,flag,score)
    elif command =="p":
        print_all()
    elif command =="r":
        read_data(input("읽어들일 파일 경로를 입력하세요 :"))
    elif command =="s":
        sort_entry(input("어떤 순서로 정렬 할까요? n : 이름순 , a : 평균점수순, g : grade순"))
    elif command =='w':
        write_data(input("경로를 입력하세요"))

