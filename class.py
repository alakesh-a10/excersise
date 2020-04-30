class cls():
    def __init__(self,std='',sec=''):
        sef.std=std
        self.sec=sec
class student(cls):
    acess_level='student'
    def __init__(self,name,age,std,sec):
        self.name=name
        self.age=age
        self.sec=sec
        self.std=std
    def display(self):
        print("Name    :",self.name)
        print("Age  :",self.age)
        print("Standard    :",self.std)
        print("Section  :",self.sec)

x=student(name="Alakesh", age=15,std=10,sec='vivek')
x.display()
y=student(name="Vikash", age=12,std=6,sec='Anand')
y.display()
print("\n")
print(type(x))
