
# x=5
# if(x<1):
#     print("Hello")
#     print("Hi")  
# else:
#     print("HOO")    

# a=5
# while(a:=10):
#     print("Hello")
#     break
# print("India")



# class PlatformSerializer(serializer.ModelSerialzier):
#     movie = WatchlistSerializer(read_only=True)

#     class Meta:
#         model=Stream
#         fields="__all__"


# class Person:
#     def __init__(self):
#         name="Jay"
#         age=21
# print(Person().name)
# print(Person().age)



# class Student:
#     def __init__(self,name,marks1,marks2,marks3):
#         self.name=name
#         self.marks1=marks1
#         self.marks2=marks2
#         self.marks3=marks3

#     def avg(self):
#        return (self.marks1 + self.marks2 + self.marks3)/3
            
# s1= (Student("jay",12,56,99))           
# print(s1.avg())

# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        

#     def avg(self):
#        sum=0
#        if len(self.marks)<=3:
#            for val in self.marks:
#                sum+=val
#            return (sum/3)
#        else:
#            return ("enter marks of 3 subjects only")
# s1= (Student("jay",[12,56,99]))           
# print(s1.avg())



############        SLI                   ##########3333
# class Parent:

#     @staticmethod
#     def car():
#         return("This is parents car")

#     @staticmethod
#     def house():
#         return("This is parents house")


# class Child(Parent):
#     def __init__(self,name):
#         self.name=name

# cl=Child("Neel")
# print(cl.car())



# class Parent:

#     @staticmethod
#     def car():
#         return("This is parents car")

#     @staticmethod
#     def house():
#         return("This is parents house")


# class Child(Parent):
#     def __init__(self,name):
#         self.name=name

# class GrandChild(Child):
#     def __init__(self,parent_name):
#         self.parent_name=parent_name
# cl=GrandChild("Nep")
# print(cl.car())


# class Parent:
#     def __init__(self, age):
#         self.age = age

#     @staticmethod
#     def car():
#         print("This is parents car")

#     @staticmethod
#     def house():
#         return("This is parents house")

# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(age)
#         self.name = name
#         super().car()


# cl=Child("Nep",12)
# print(cl.age)
# print(Parent.age)
# print(cl.name)
# print(cl.car())


# class Person:
#     name="anonymous"

#     def name_of_person(self,name):
#         self.name=name
#         # Person.name=name
#         # self.__class__.name=name

# p1 = Person()
# p1.name_of_person("jay")
# print(p1.name)
# print(Person.name)


# class Person:
#     name="anonymous"

#     @classmethod
#     def name_of_person(cls,name):
#         cls.name=name
        
# p1 = Person()
# p1.name_of_person("jay")
# print(p1.name)
# print(Person.name)


# class Person:

#     def __init__(self,phy,che,mat):
#         self.phy=phy
#         self.che=che
#         self.mat=mat

#     @property
#     def percentage(self):
#         return str((self.phy+self.che+self.mat)/3) + "%"
    
#     def name_of_per(self,name):
#         self.name=name
        
# p=Person(80,80,80)
# print(p.percentage)
# p.name_of_per("jay")
# print(p.name)
# p.phy=79
# print(p.percentage)




# class ComplexNum:

#     def __init__(self,num1,num2):
#         self.num1=num1
#         self.num2=num2
        
#     def compl_num(self):
#         print(f"{self.num1} i + {self.num2} j")
        
#     def add(self,sec):
#         real=self.num1+sec.num1
#         img=self.num2+sec.num2
#         return ComplexNum(real,img)

# c1=ComplexNum(8,11)
# c1.compl_num()

      
# c2=ComplexNum(3,9)
# c2.compl_num()

# c3=c1.add(c2)
# c3.compl_num()






class ComplexNum:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def compl_num(self):
        print(f"{self.num1} i + {self.num2} j")
        
    def __add__(self,sec):
        real=self.num1+sec.num1
        img=self.num2+sec.num2
        return ComplexNum(real,img)

c1=ComplexNum(8,11)
c1.compl_num()

      
c2=ComplexNum(3,9)
c2.compl_num()

c3=c1+c2
c3.compl_num()