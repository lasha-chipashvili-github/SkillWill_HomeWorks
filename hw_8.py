from abc import ABC, abstractmethod

class Person(ABC):
    
    @abstractmethod
    def display_details(self):
        pass


class InfoMixin:
    def info(self):
        info = dict((key,value) for key,value in self.__dict__.items())
        
        for key, value in info.items():
            print(f"{key.capitalize()}: [{value}].")            
        return None


class Student(Person, InfoMixin):
       
    def __init__(self, student_id, name, subject):
        self.subject = subject        
        self.grades = {f'{self.subject}': []}
        self.__student_id = student_id
        self.name = name
        
        
    def add_grade(self, subject, *grade):
        self.grade = grade
        for grd in self.grade:
            self.grades[self.subject].append(grd)
        
    @property
    def avarage_grade(self):
        return sum(self.grades[self.subject])/len(self.grades[self.subject])
    
    def display_details(self):
        print(f"Studen's id: {self.student_id}\nStudent's name: {self.name}\nStudent's avarage grade: {self.avarage_grade}")



class StudentManagementSystem():

    def __init__(self):
        self.subjects = {'python', 'JS', 'CPP'}
        self.students = {}
        
    
    def add_student(self, student_id:int, name:str, subject:str):
        if student_id in self.students:
            print(f"სტუდენტი {student_id}-ით უკვე არსებობს.")
            return 1
        new_student = Student(student_id, name, subject)
        self.students[student_id] = new_student
        print("ახალი სტუდენტი დაემატა!")
        
        
    def show_student_details(self, student_id):
        student = self.students.get(student_id)
        name = student.name
        avg = student.avarage_grade
        grd = student.grades
        return (f"Student's name: {name} \nStudent's grades: {grd} \nStudent's avarage grade: {avg}")

    
    def show_student_avarage_grade(self, student_id):
        return self.students.get(student_id).avarage_grade

        


if __name__ == '__main__':    
    uni = StudentManagementSystem()
    student1 = uni.add_student(1,'lasha','python')
    student1 = uni.students.get(1)
    student1.add_grade('python', 100, 95, 99)
    print("საშუალო ქულაა: ", uni.show_student_avarage_grade(1))
    print(uni.show_student_details(1))
    