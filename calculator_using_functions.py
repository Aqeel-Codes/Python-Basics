# Calculator in python using functions
oprtr = input("Enter the operator sign (+, -, * ,/ ,// ,% ,^2) which one you want to perform : ")
def sum(num1,num2):
	return num1+num2
def sub(num1,num2):
	return num1-num2
def mul(num1,num2):
	return num1*num2
def divide(num1,num2):
	return num1/num2
def floor_division(num1,num2):
	return num1//num2
def mod(num1,num2):
	return num1%num2
def sqr(num1):
	return num1*num1

if oprtr == '^2':
   num1 = int(input("Enter the first integer :  "))
   print("The square of ",num1," is : ",sqr(num1))
else:
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   if oprtr == '+':
      print("The result of ",num1," + ",num2," is : ",sum(num1,num2))
   elif oprtr == '-':
   	print("The result of ",num1," - ",num2," is : ",sub(num1,num2))
   elif oprtr == '*':
   	print("The result of ",num1," x ",num2," is : ",mul(num1,num2))
   elif oprtr == '/':
       print("The result of ",num1," x ",num2," is : ",divide(num1,num2))
   elif oprtr == '//':
   	print("The result of ",num1," x ",num2," is : ",floor_division(num1,num2))
   elif oprtr == '%':
   	print("The result of ",num1," x ",num2," is : ",mod(num1,num2))
   else:
        print("You put wrong operator.")