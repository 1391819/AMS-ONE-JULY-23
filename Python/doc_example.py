class Example():
    '''
    Example: an example class for documentation
    '''
    def __init__(self) -> None:
        pass

    def factorial(x: int) -> int:
        '''
        factorial(x): Returns the product of all of the integers from 1 to x inclusive
        '''
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

if __name__ == '__main__':
    print(Example.factorial(3))
    print(Example.factorial(5))
    print(Example.factorial(10))