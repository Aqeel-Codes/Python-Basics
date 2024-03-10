# Calculator in python
oprtr = input("Enter the operator sign (+, -, * ,/ ,// ,% ,^2) which one you want to perform : ")

if oprtr == '+':
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   print("The result of ",num1," + ",num2," is : ",num1+num2)
elif oprtr == '-':
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   print("The result of ",num1," - ",num2," is : ",num1-num2)
elif oprtr == '*':
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   print("The result of ",num1," x ",num2," is : ",num1*num2)
elif oprtr == '/':
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   print("The result of ",num1," / ",num2," is : ",num1/num2)
elif oprtr == '//':
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   print("The result of ",num1," // ",num2," is : ",num1//num2)
elif oprtr == '%':
   num1 = int(input("Enter the first integer :  "))
   num2 = int(input("Enter the second integer:  "))
   print("The result of ",num1," % ",num2,"is : ",num1%num2)
elif oprtr == '^2':
   num1 = int(input("Enter the first integer :  "))
   print("The square of ",num1," is : ",num1*num1)
else:
   print("You put wrong operator.")