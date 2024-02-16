from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def get_sinfo(self):
        pass
    @staticmethod
    def school_info():
        print("School name: ",School.school_name)

class School(Person):
    school_name = "AVKC"
    stu_count = 0
    @classmethod
    def total_children(cls):
        print("School name is ",cls.school_name,"count:",cls.stu_count)

    def __init__(self,sid,DOJ,Class):
        self.sid = sid
        self.DOJ = DOJ
        self.Class = Class
        School.stu_count += 1
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):
        print(a+b+c)
    @classmethod
    def school_Name(cls):
        print("School name: ",cls.school_name)
    def get_sinfo(self):
        print("Student info: ",self.sid,self.DOJ,self.Class)
Kumar = School(123,"12-7-2023","7th")
Kesavan = School(123,"12-7-2023","10th")
Aryadeep = School(122,"12-4-2022","9th")
Kumar.get_sinfo()
School.total_children()
School.school_Name()
Person.school_info() #static method calling using classname
Kumar.school_Name()#method calling using objectname
Kesavan.school_info()#method calling using objectname
School.get_sinfo(Kumar)#method calling using objectname
Aryadeep.get_sinfo()
Kesavan.get_sinfo()
Kumar.sum(2,4,5)
class Teacher(School):
    teacher_count = 0
    def __init__(self,subject,grade):
        self.subject = subject
        self.grade = grade
        Teacher.teacher_count += 1
Ramya = Teacher("English","senior")
print("Teacher count: ",Teacher.teacher_count)
