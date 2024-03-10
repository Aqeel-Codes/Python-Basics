# Calculator in python
num1 = int(input("Enter the first integer :  "))
num2 = int(input("Enter the second integer:  "))
oprtr = input("Enter the operator sign (+, -, * ,/ ,// ,% ,^2) which one you want to perform : ")

if oprtr == '+':
   print("The result of ",num1," + ",num2," is : ",num1+num2)
elif oprtr == '-':
   print("The result of ",num1," - ",num2," is : ",num1-num2)
elif oprtr == '*':
   print("The result of ",num1," x ",num2," is : ",num1*num2)
elif oprtr == '/':
   print("The result of ",num1," / ",num2," is : ",num1/num2)
elif oprtr == '//':
   print("The result of ",num1," // ",num2," is : ",num1//num2)
elif oprtr == '%':
   print("The result of ",num1," % ",num2,"is : ",num1%num2)
elif oprtr == '^2':
   print("The square of ",num1," is : ",num1*num1," \nThe square of ",num2," is : ",num2*num2)
else:
   print("You put wrong operator.")