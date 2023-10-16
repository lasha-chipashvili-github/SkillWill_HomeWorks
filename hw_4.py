class Student:
    university = 'ლომონოსოვის უნივერსიტეტი'
    
    def __init__(self, name:str, grade:int, age:int):
        self.name = name
        self.grade = grade
        self.age = age
    
    def __str__(self):
        return f"Name: [{self.name}], Age: [{self.age}], Grade: [{self.grade}]"
    
    
    @property
    def is_passing(self):
        if self.grade > 60:
            return True
        return False
    
    def increase_grade(self, grade):
        self.grade += grade
        return self.grade
        
    
if __name__ == "__main__":
    student = Student("დ'არტანიანი", 60, 26)
    print(student.__str__())
    print(student.is_passing)
    student.increase_grade(1)
    print(student.__str__())
    print(student.is_passing)