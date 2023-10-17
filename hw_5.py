class Person:
    def __init__(self, name:str, surname:str, age:int):
        self.name = name
        self.surname = surname
        self.age = age
       
class InfoMixin:
    def info(self):
        info = dict((key,value) for key,value in self.__dict__.items())
        
        for key, value in info.items():
            print(f"{key.capitalize()}: [{value}].")
            
        return None
        
    def __str__(self):
        return f"Name: [{self.name}], Surname: [{self.surname}], Age: [{self.age}],  University: [{self.university}]]"
    
    def return_dict(self):
        return self.__dict__
    
   
class Student(Person, InfoMixin):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university
        

if __name__ == "__main__":
    student = Student('შარლი', "დ'არტანიანი", 26, 'ლომონოსოვის უნივერსიტეტი')
    print("____1-ლი განხორციელება____")
    print(student.return_dict())
    print("____მე-2 განხორციელება____")
    student.info()
    print("____მე-3 განხორციელება____")
    print(student.__str__())  