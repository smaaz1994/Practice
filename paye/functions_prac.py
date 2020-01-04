def arithmetic_operations():
    print("Hello I'm inside a Function")
    print("Hello I'm inside a Function")
    print("Hello I'm inside a Function")
    print("Hello I'm inside a Function")

#Calculator as a Function

def calculator():
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

# calculator()

#if you want to assign a default argument to perform when a value is not provided you can
#use [def function(operand, operand2, operator = '+')] this is called a keyword argument

# def function_with_variable_args(**all_params):
#     print(all_params)
# function_with_variable_args(Name='Amjad')
# function_with_variable_args(Name='Ali', Age=50)
# # function_with_variable_args(1, 2, True)

