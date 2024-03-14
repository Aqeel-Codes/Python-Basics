# converting temperature from celcius to Fahrenheit and Fahrenheit to celcius
temp = float(input("Enter the temperature in celcius : "))
unit = input("Enter the unit of temperature : ")
def temp_converter(temp,unit):
	if unit == 'c':
		cnvrtr = (9/5 * temp) + 32
		r = round(cnvrtr,2)
		return (f"After converting celcius to fahrenheit is : {r}F")
	else:
		cnvrtr = (temp - 32) * 5/9
		r = round(cnvrtr,2)
		return (f"After converting fahrenheit to celcius is : {r}C")


print(temp_converter(temp,unit))
