class circle():
    #class object attribute
    pi=3.14
    A=0
    def __init__(self, radius=1):
        self.radius=radius
    def area(self):
        circle.A=self.radius*self.radius*self.pi
    def display(self):
        print("the Area is:",circle.A)
        print("The Circumference is: ",2*circle.pi*self.radius)
print("Example of class to calculate Area and Circumference of a Circle")
print("Trying push By fetching at first")        
c=circle()
c.area()
c.display()
