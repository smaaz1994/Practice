# for x in range(2,50):
#     print(x,end=" ")

# 3 Programs with same result but different syntax and no. of iterations

# for num in range(101):
#     if (num%2)==0:
#         print(num, end=" ")

# for num in range(51):
#     print(num*2, end=" ")

# for num in range(0, 101, 2):
#     print(num, end=" ")

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print("Before Append ", numbers)
# numbers.append(11)
# print("After Append ", numbers)
# numbers.insert(2, 22)
# print("After Insert ", numbers)
# del numbers[2] #square bracket indicates index
# print("After Delete ", numbers)
# numbers.remove(11) #It deletes only the first instance of the number if two instances are present. 
# print("After Remove ", numbers) # Can call multiple times if you want to remove multiple instances of the same number.

##Loops

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# for i in range(len(numbers)):
#     print(numbers[i], end=" || ")

#Assignment = Take input and determine whether it is prime or not

# for x in range(1,11):
#     print("2 x " + str(x) + " = " + str(2*x))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 4, 9, 10, 11, 4, 12]
# hetro_list = ["Amjad", 2, 1.6, True, "Hello"]
# print("Original list= ")
# print(hetro_list)
# hetro_list[2] = 3.6 #editing list data
# hetro_list[4] = "Hi"
# print("Edited list= ")
# print(hetro_list)

#ASSIGNMENT (remove multiple similar values from list using loop)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 4, 9, 10, 11, 4, 12]

# print("Original = ", numbers)
# for i in range(len(numbers)):
#     numbers.remove(4)
#     if 4 not in numbers:
#         break
# print("Element 4 Removed = ", numbers)

# ANOTHER METHOD

# print("Original = ", numbers)
# for i in numbers:
#     if i==4:
#         numbers.remove(4)
# print("All 4s Removed = ", numbers)

