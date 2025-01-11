#Compile-Time Polymorphism
#In compile-time polymorphism, the function to be called is determined at compile time.
class Calculator:
    def add(self,a,b=0,c=0):
        return a+b+c
    
calc=Calculator()
print(calc.add(5)) #Single arguement
print(calc.add(5,10)) #Two arguement
print(calc.add(5,10,15)) #Three arguement