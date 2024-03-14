# Function for finding the maximum number among 3 parameters
num1 = int(input("Enter 1st integer :"))
num2 = int(input("Enter 2nd integer :"))
num3 = int(input("Enter 3rd integer :"))
def max(num1,num2,num3):
	if num1 >= num2:
		if num1>=num3:
			return num1
		else:
			return num3
	elif num2 >=num1:
		if num2>=num3:
			return num2
		else:
			return  num3

print(f"The max number between {num1},{num2},{num3} is : ",max(num1,num2,num3))