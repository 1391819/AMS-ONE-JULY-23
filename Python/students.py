class Student():
    '''
    A class which represents students. Students have a name, an age and a class 
    - the default class is 'student'. 
    '''
    def __init__(self, name: str, age: int, class_: str = 'Student') -> None:
        self.name = name
        self.age = age
        self.class_ = class_
    
    def calculate_avg(self, assessment1: int, assessment2: int, assessment3: int) -> float:
        '''
        This function takes 3 assessment scores as input, prints a message stating
        the average score to 2 dp, and then returns this average
        '''
        avg = (assessment1 + assessment2 + assessment3) / 3
        print(f"{self.name}'s average is {avg:.2f}")
        return avg

    def __str__(self):
        return f"{self.name}, {self.age}: {self.class_}"

if __name__ == '__main__':
    stu1 = Student("Alice", 20, "Physics")
    stu2 = Student("Bob", 19, "English Literature")
    stu1_avg = stu1.calculate_avg(97, 80, 86)
    stu2_avg = stu2.calculate_avg(90, 76, 92)