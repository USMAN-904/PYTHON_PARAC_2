
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def permeter(self):
        return 2 * 3.14 * self.radius
    
Circle_1 = Circle(4)
print('Area=', Circle_1.area())
print('perimeter=', Circle_1.permeter())