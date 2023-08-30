
import termcolor
from calc2 import Calc

class calcaulater(Calc):
    def hello():
        print(termcolor.colored("Application calcaulater" , color='yellow'))
    def get_numbers():
        calcaulater.hello()
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        return num1, num2

    def get_operator():
        operator = input( "Please type an operation you would it :  \n + , - , * , / ==> ")
        return operator
    @classmethod
    def again(cls):

        calcaulater_again = input('Do you want to calculate again? \n Please type Y for YES or N for NO.')

        if calcaulater_again.upper() == 'Y':  # y or Y 
            calcaulater.calculate()

        elif calcaulater_again.upper() == 'N':
            print(termcolor.colored("See you later." , color='blue'))

        else:
            calcaulater.again()

    @classmethod
    def calculate(cls):
        num1, num2 = cls.get_numbers()
        operator = cls.get_operator()
        if operator == '+':
            print (cls.add(num1, num2))
        elif operator == '-':
            print (cls.sub(num1, num2))
        elif operator == '*':
            print (cls.mul(num1, num2))
        elif operator == '/':
            print (cls.div(num1, num2))
        else:
            print(f'{termcolor.colored("ERROR" , color="red")}, please run the program again.')
        
        calcaulater.again()


calcaulater.calculate()

