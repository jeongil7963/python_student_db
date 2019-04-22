import re
import sys

# studentList : student 객체를 관리할 리스트
# _ids : index 기준값으로 활용
studentList = []
_ids = 0


# Class Student : 학생들의 정보를 클래스 객체로 활용
class Student:

    # 클래스 선언 시 변수 초기화
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

    # 시험 점수 변경 시 평균, 등급 변경
    def refresh(self):
        self.average = ( float(self.mid_score) + float(self.last_score))/2
        self.grade = calculate_grade(self.average)

    # 학생 정보 출력
    def print(self):
        print("%6s %10s %6s %12s %6s %6s %6s %6s"
                %(str(self.idx), self.id, self.name, self.birth,
                self.mid_score, self.last_score, self.average, self.grade))
	
	# 객체간 동일여부를 체크하기 위해 __eq__ 함수 오버라이딩      
    def __eq__(self, other):
        return ( self.id , self.name, self.birth, self.mid_score, self.last_score )  == ( other.id , other.name, other.birth, other.mid_score, other.last_score )
    
	# set(객체)이 가능하도록 __hash__ 함수 오버라이딩
    def __hash__(self):
        return hash((self.id , self.name, self.birth, self.mid_score, self.last_score))


# 입력한 학생 정보 유효성 체크
def regular_verification(id_, name_, birth_, mid_score_, last_score_):
    
    # 점수가 100점을 넘은 경우 False return
    if ( int(mid_score_) > 100 ) or ( int(last_score_) > 100 ) :
        return False

    # 정규식 작성
    re_id = re.match('^2019[0-9]{4}$', id_)
    re_name = re.match('^[가-힣]*$', name_)
    re_birth = re.match('^(19|20)\d{2}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[0-1])$', birth_)
    re_mid_score = re.match('^[0-9]{1,3}$', mid_score_)
    re_last_score = re.match('^[0-9]{1,3}$', last_score_)

    # 유효 체크 결과값을 리스트에 삽입
    re_list = []
    re_list.append(re_id)
    re_list.append(re_name)
    re_list.append(re_birth)
    re_list.append(re_mid_score)
    re_list.append(re_last_score)

    # 결과값 유효하지 않은 경우 false return
    for re_val in re_list:
        if re_val == None:
            return False

    # 유효한 경우 true return
    return True


# 헤더 출력
def print_view():
    print("%6s %10s %9s %12s %6s %6s %6s %6s" %("index", "id", "name", "birth", "mid", "final", "avg", "grade"))


# 평균 값을 통한 등급 계산
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


# 학생 정보 리스트에 추가
def add_a_new_entry():
    print("Start adding a new entry")
    input_id = input("Enter student id(2019xxxx) : ")
    input_name = input("Enter student name(Only Hangul) : ")
    input_birth = input("Enter student birth(yyyy-mm-dd) : ")
    input_mid_score = input("Enter student mid score(0~100) : ")
    input_final_score = input("Enter student final score(0~100) : ")

    # 학생 정보 유효성 체크
    if regular_verification(input_id, input_name, input_birth, input_mid_score, input_final_score) == False:
        print("Input Student Value Error")
        return
    
    # 유효한 경우 리스트 추가
    student_object = Student(input_id, input_name, input_birth, input_mid_score, input_final_score)
    studentList.append(student_object)


# 학생 정보 삭제
def delete_an_entry():

    # 삭제할 학생 정보 입력
    print("Start deleting an entry")
    id_or_name_val = input("Enter Student Id or Name : ")
    idx = 0

    # 학생 정보가 일치하는 경우 index 값을 받아옴
    for student in studentList:
        if student.name == id_or_name_val:
            idx = student.idx

        elif student.id == id_or_name_val:
            idx = student.idx

    # index 값을 받아오지 못한 경우 return
    if idx == 0:
        print("Input Value Error")
        return

    # index 값을 받아온 경우
    # 정말 삭제할 것인지 확인 후 삭제 진행
    else:
        d_check = input("Do you really delete this one?(Y/N)").lower()

        if d_check == "y":
            studentList.pop(idx-1)

            for num in range(idx-1, len(studentList)):
                studentList[num].idx = num+1
            
            global _ids
            _ids -= 1
            print("Proceed with the deletion.")

        elif d_check == "n":
            print("Cancel deletion.")

        else:
            print("Input Value Error")



# 학생 정보 찾기
def find_some_item_from_entry():

    # 찾을 학생 정보 입력
    print("Start find some item from entry")
    id_or_name_val = input("Enter Student Id or Name : ")
    idx = 0

    # 학생 정보가 일치한 경우 index 값을 받아옴
    for student in studentList:
        if student.name == id_or_name_val:
            idx = student.idx

        elif student.id == id_or_name_val:
            idx = student.idx
    
    # index 값을 받아오지 못한 경우 메세지 출력
    if idx == 0:
        print("No matching values found.")
    
    # index 값을 받아온 경우, 해당 학생의 평균과 학점 출력
    else:
        print("Print the average score and grade of a student")
        print("Average score : ", studentList[idx - 1].average)
        print("Grade : ", studentList[idx - 1].grade)


# 학생 정보 수정 기능 
def modify_an_entry():

    # 수정할 학생 정보 입력
    print("Start modifying an entry")
    id_or_name_val = input("Enter Student Id or Name : ")
    idx = 0

    # 일치하는 경우 index 값을 받아옴
    for student in studentList:
        if student.name == id_or_name_val:
            idx = student.idx

        elif student.id == id_or_name_val:
            idx = student.idx

    # index 값을 받지 못한 경우 return
    if idx == 0:
        print("No matching values found.")
        return
    
    # index 값을 받아온 경우
    else:

        # 수정할 중간고사, 기말고사 선택
        print("Which score do you want to change?(mid_term: m, final: f)")
        input_val = input("Enter m(mid_term) or f(final_term) : ")
        input_val.lower();

        # 해당하는 시험 점수 수정
        # 평균, 학점 수정
        print("Student idx : ", idx)
        if input_val == "m":
            input_mid_score_val = input("Enter mid score to modify : ")
            studentList[idx - 1].mid_score = input_mid_score_val
            studentList[idx - 1].refresh()
        elif input_val == "f":
            input_final_score_val = input("Enter final score to modify : ")
            studentList[idx - 1].final_score = input_final_score_val
            studentList[idx - 1].refresh()
        else:
            print("Input Value Error")
            return

    # 수정한 내용 출력
    print("Please check the modified details")
    print_view()
    studentList[idx - 1].print()


# 학생 전체 정보 출력
def print_the_contents_of_all_entries():
    print("Start printing the contents of all entries")
    print_view()
    for student in studentList:
        student.print()


# 파일 데이터 불러오기, 검증 후 추가
def read_personal_data_from_a_file():
    print("Start reading personal data from a file")
    file_data = input("Enter the file name : ")
    try:
        data = open(file_data)

        for each_line in data:
            try:
                student_val = each_line.split("\t")
                student_val[5] = student_val[5][:-1]
                
                # 학생 정보 값이 잘못된 경우 리스트에 추가하지 않고 다음으로 넘어감
                if regular_verification(student_val[1], student_val[2], student_val[3], student_val[4], student_val[5]) == False:
                    continue

                student_object = Student(student_val[1], student_val[2], student_val[3], student_val[4], student_val[5])
                studentList.append(student_object)
            except:
                print("Unexpected Error : ", sys.exc_info())

        data.close()

    except IOError:
        print('The datafile is missing.')


# 학생 데이터 정렬 기능
def sort_entries():

    # 정렬할 데이터 범주 입력 받기
    print("Start sorting entries")
    input_val = input("Enter n(name) or a(average) or g(grade) : ")
    input_val.lower

    if input_val == "n":
        studentList.sort( key = lambda object:object.name, reverse=False)

    elif input_val == "a":
        studentList.sort( key = lambda object:object.average, reverse=True)

    elif input_val == "g":
        studentList.sort( key = lambda object:object.grade, reverse=True)

    else:
        print("Input Value Error")
        return

    # 정렬한 데이터 출력 후
    # index 값으로 재정렬
    print("Please check the modified details")
    print_view()
    print_the_contents_of_all_entries()
    studentList.sort( key = lambda object:object.idx, reverse=False)


# 프로그램 종료
def quit():
    print("Start quitting the program")
    return False


# 파일 데이터 쓰기
def write_the_contents_to_the_same_file():

    # 저장할 파일 이름 입력 받기
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

		
# 중복되는 entry 를 삭제

def erase_duplicates():
	global studentList
	studentList = list(set(studentList))
	for i,student in enumerate(studentList):
		student.idx = i+1

# 학생 정보 프로그램 시작
def db_start():
    print("Start student Database Program")
    flag_quit = True

    # quit 함수 호출 전 까지 while 문 반복
    while flag_quit:
        print(" a: add a new entry\n"
          ,"d: delete an entry\n"
          ,"f: find some item from entry\n"
          ,"m: modify an entry\n"
          ,"p: print the contents of all entries\n"
          ,"r: read personal data from a file\n"
          ,"s: sort entries\n"
          ,"q: quit\n"
          ,"w: write the contents to the same files\n"
		  ,"e: erase all duplicated entries")

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
			
        elif input_val == 'e':
            erase_duplicates()

        else:
            print("Input Value Error")


if __name__ == '__main__':

    # 학생 정보 프로그램 시작 함수 호출
    db_start()