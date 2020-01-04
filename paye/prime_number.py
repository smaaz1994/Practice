#PROGRAM FOR PRIME NUMBERS

num = int(input("Enter a number to check if it is prime or not: "))
 
for i in range(2, num):
	if num % i  == 0:
		print("Not a Prime number")
		break
else:
	print("Prime number")