print("=================================================================")


num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
operatorsign = input("Enter Operator: ")
answer = 0

print("=================================================================")


if operatorsign == "+":
    answer = num1 + num2
    print("The result of adding these two numbers is ", answer)

elif operatorsign == "-":
    answer = num1 - num2
    print("The result of subtracting these two numbers is ", answer)

elif operatorsign == "*":
    answer = num1 * num2
    print("The result of multiplying these two numbers is ", answer)

elif operatorsign == "/":
    answer = num1 / num2
    print("The result of dividing these two numbers is ", answer)

elif operatorsign == "**":
    answer = num1 ** num2
    print("The result of "+str(num1)+" exponent "+str(num2)+" is ", answer)

elif operatorsign == "%":
    answer = (num1 / num2) * 100
    print("The "+str(num1)+" is "+str(answer)+"% "+"of",num2)

else:
    print("Invalid operator")

print("=================================================================")
