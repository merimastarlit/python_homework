# Task 5
#%%
# creating classical version pf a parent class Point
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __eq__(self, other_point):
        return self.x == other_point.x and self.y == other_point.y
    # euclidean distance between two points:
    def distance(self, other_point):
        return ((self.x - other_point.x)**2 + (self.y - other_point.y)**2) ** 0.5

        
    
# creating a child class Vector that extends Point
class Vector(Point):


    def __init__(self, x, y):
        super().__init__(x, y)

        #customizing the string representation for the child to be different from the parent 
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    # adding two vectors
    def __add__(self, other_point):
        new_x = self. x + other_point.x
        new_y = self.y + other_point.y
        return Vector(new_x, new_y)
    
# testing the classes
example_point1 = Point(1, 2)
example_point2 = Vector(4, 6)

print(example_point1)
print(example_point2)

# %%
