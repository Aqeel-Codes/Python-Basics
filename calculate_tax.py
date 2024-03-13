# calculate 16 percent tax using function
amount = float(input("Enter your amount to calculate tax : "))
tax_prcnt = float(input("Enter the tax percentage : "))
def tax_16(amount):
	tax = (amount * tax_prcnt)/100
	return tax
print(f"The {tax_prcnt}%tax of your amount is ",tax_16(amount))