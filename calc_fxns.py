
def getNumbers():
	num1, num2 = 0.0, 0.0

	try:
		num1 = float(input("Enter number 1:  "))
	except ValueError:
		print("That was not a float. Please try again.")

	try: 
		num2 = float(input("Enter number 2: "))
	except ValueError:
		print("That was not a float. Please try again.")
	return num1, num2

def add(a,b):
	return a + b

def subtract(a,b):
	return a - b

def multiply(a,b):
	return a * b

def divide(a, b):
	return a / b



