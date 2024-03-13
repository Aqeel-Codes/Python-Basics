# converting temperature from celcius to Fahrenheit and Fahrenheit to celcius
ask = input("Enter the temerature unit in which you want to convert your like f or c : ")
def c_to_f(temp):
	cnvrtr = (9/5 * temp) + 32
	r = round(cnvrtr,2)
	return r
def f_to_c(temp1):
	cnvrtr = (temp1 - 32) * 5/9
	r = round(cnvrtr,2)
	return r
if ask == 'c':
	temp = float(input("Enter the temperature in celcius : "))
	print("Celcius temperature in fahrenheit is : ",c_to_f(temp),"°F")
else:
	temp1 = float(input("Enter the temperature in fahrenheit : "))
	print("Fahrenheit temperature in celcius is : ",f_to_c(temp1),"°C")


