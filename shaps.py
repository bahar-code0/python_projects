class shape:
    def perimeter(self):
         pass

    def area(self):
         pass


class Circle(shape):
    def __init__(self,radius):
         self.radius=radius

    def perimeter(self):
         return 2*self.radius*3.14

    def area(self):
         return self.radius**2*3.14

class Squar(shape):
    def __init__(self,side):
         self.side=side

    def perimeter(self):
         return self.side*4

    def area(self):
         return self.side**2

class Rectangle(shape):
    def __init__(self,wid,leng):
         self.wid=wid
         self.leng=leng

    def perimeter(self):
         return (self.wid+self.leng)*2

    def area(self):
         return self.wid+self.leng

class Triangle(shape):
    def __init__(self,side):
         self.side=side

    def perimeter(self):
         return self.side*3

    def area(self):
         return ((3**0.5)/4)*(self.side**2)           
    

shapes=input("Enter the character of the shape:(c.Circle,s.Square,r.Rectangle,t.Triangle)")

if shapes == 'c':
     radius=float(input("Enter the radius:"))
     circle=Circle(radius)
     print(f"perimeter={circle.perimeter()}")
     print(f"area={circle.area()}")
elif shapes == 's':
     side=float(input("Enter the side:"))
     squar=Squar(side)
     print(f"perimeter={squar.perimeter()}")
     print(f"area={squar.area()}")
elif shapes == 'r':
     wid=float(input("Enter the width:"))
     leng=float(input("Enter the length:"))
     rectangle=Rectangle(wid,leng)
     print(f"perimeter={rectangle.perimeter()}")
     print(f"area={rectangle.area()}")
elif shapes == 't':
     side=float(input("Enter the side:"))
     triangle=Triangle(side)
     print(f"perimeter={triangle.perimeter()}")
     print(f"area={triangle.area()}")
else:
     print("Enter(c,s,r,t)")
