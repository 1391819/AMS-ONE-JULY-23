class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __add__(self, rect2):
        return Rectangle(self.width + rect2.width, self.height + rect2.height)
    
    def __str__(self):
        return ('+' * self.width + '\n') \
            + '\n'.join('+' + (self.width - 2) * ' ' + '+' for _ in range(self.height - 2)) \
            + '\n' + ('+' * self.width + '\n')
    
    def calculate_area(self):
        return self.width * self.height
    
    def __int__(self):
        return self.calculate_area()

if __name__ == '__main__':
    rect1 = Rectangle(5, 3)
    print(rect1)
    rect2 = Rectangle(2, 7)
    print(rect2)
    print(rect1 + rect2)
    print(int(rect1 + rect2))