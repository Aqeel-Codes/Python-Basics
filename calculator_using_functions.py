# Calculator in python using functions
oprtr = input("Enter the operator sign (+, -, * ,/ ,// ,% ,^2) which one you want to perform : ")
def sum(num1,num2):
	print("The result of ",num1," + ",num2," is : ",num1+num2)
def sub(num1,num2):
	print("The result of ",num1," - ",num2," is : ",num1-num2)
def mul(num1,num2):
	print("The result of ",num1," x ",num2," is : ",num1*num2)
def divide(num1,num2):
	print("The result of ",num1," / ",num2," is : ",num1/num2)
def floor_division(num1,num2):
	print("The result of ",num1," // ",num2," is : ",num1//num2)
def mod(num1,num2):
	print("The result of ",num1," % ",num2," is : ",num1%num2)
def sqr(num1):
	print("The square of ",num1," is : ",num1*num1)

if oprtr == '^2':
   num1 = int(input("Enter the first integer :  "))
   print(sqr(num1))
else:
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   if oprtr == '+':
      print(sum(num1,num2))
   elif oprtr == '-':
   	print(sub(num1,num2))
   elif oprtr == '*':
   	print(mul(num1,num2)) 
   elif oprtr == '/':
       print(divide(num1,num2))
   elif oprtr == '//':
   	print(floor_division(num1,num2))
   elif oprtr == '%':
   	print(mod(num1,num2))
   else:
        print("You put wrong operator.")