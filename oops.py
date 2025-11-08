# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def details(self):
#         return f"student name is {self.name} and his age is {self.age}"
        
# s1=Student("jay",90)
# print(s1.details())






# class Student:
#     def __init__(self,name,age,percentage):
#         self.name=name
#         self.age=age
#         self.__percentage=percentage
    
#     def details(self):
#         return f"student name is {self.name} and his age is {self.age}"
#     def get_percentage(self):
#         return self.__percentage
# s1=Student("jay",20,90)
# print(s1.details())
# print(s1.get_percentage())
# print(s1.name)
# print(s1.__percentage)



###Inheritance#######

# class Student:
#     def __init__(self,name,age,percentage):
#         self.name=name
#         self.age=age
#         self.percentage=percentage
    
#     def details(self):
#         print(f"student name is {self.name} and his age is {self.age} and has {self.percentage} percentage")

# class GraduateStudent(Student):
#     def __init__(self,name,age,percentage,stream):
#         super().__init__(name,age,percentage)
#         self.stream=stream
#     def graduate_details(self):
#         super().details()
#         # return f"{dtls}.student stream is {self.stream}"

# s1=GraduateStudent("jay",20,90,"CS")
# s1.graduate_details()
# # print(s1.__dict__)








class Parent:
    def __init__(self,name):
        self.name=name

    
class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name)
        self.age=age

    def show(self):
        print(f"The name of person is {self.name} and its age is {self.age}")
# p1=Parent("John")        
# p1.show()

c1=Child("KSO",93)
c1.show()