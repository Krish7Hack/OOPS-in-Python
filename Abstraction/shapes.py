
class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length #Both are private attribute
        self.__breadth = breadth

    def get_length(self):
        return self.__length
    
    def set_length(self,length):
        if length > 0:
            self.__length = length
        else:
            print("Length must be positive number")
    
    def area(self):
        return self.__length * self.__breadth
    
    def perimeter(self):
        return 2 * (self.__length + self.__breadth)

    
