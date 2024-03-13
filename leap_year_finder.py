# finding the current year is leap year or not
year = int(input("Enter the year to check , this is leap year or not: "))
def leap_year(year):
	if year % 4 == 0:
		return print(f"{year} is leap year")
	else:
		return print(f"{year} is not a leap year")
	return 0
print(leap_year(year))


		