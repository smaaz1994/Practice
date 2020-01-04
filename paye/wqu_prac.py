def mult(numbers):
    for i in numbers:
        numbers[i] = numbers[i*10]
        i+=1
    return numbers

numbers = [1, 2, 3]
mult(numbers)
print(numbers)