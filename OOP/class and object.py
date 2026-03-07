class Student: #class
    def __init__(self):# declared function.  init is used to internally define
        self.name = 'XYZ'
        self.age = 23
        self.marks = 65
        #print("__init__ is called!")
    
    def talk(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Marks: ", self.marks)

s1 = Student() # constructor
#s1.name = 'Jhon'
s1.talk()
#print(s1.name)
print("-----------------")
s2 = Student()
#s2.name = "Rohit"
print(s2.name)
#s2.talk()
