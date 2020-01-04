# a = [1, 2, 4, 6, -1, -2, 100]
# b = []
# for i in range(2,6):
#     b.append(a[i])
# print(a)
# print(b)

#LIST SLICING

# a = [1, 2, 4, 6, -1, -2, 100]
# b = a[2:6]
# print(a)
# print(b)

# numlist1 = [1,2,3,4]
# numlist2 = numlist1
# numlist2.append(10)

# print(numlist1)
# print(numlist2)

#As seen above, in python if you change the second list, the first list is also affected.
#Because it does not treat the lists like variables. to avoid this we use copy method

# numlist1 = [1,2,3,4]
# numlist2 = numlist1.copy()
# numlist2.append(10)

# print(numlist1)
# print(numlist2)

# numlist1 = [1,2,3,4]
# a = numlist1.pop(2) #pops given index number or pops the last element if no index is given
# print(a)
# print(numlist1)


# #Multiply each element in list by 10 and create a new list
# list1=[1,2,3,4,5,6,7,8,9,10]
# list2=[]
# print(list1)
# for i in list1:
#     list2.append(i*10)
# print(list2)


# #NESTED LOOP

# my_list = ["Karachi","Lahore","Islamabad","Peshawar"]
# for i in my_list:
#     for x in range(5):
#         print(i,x)

# #Assignment : print multiplication tables of numbers input by user

# a = int(input("Enter starting range of Required Tables: "))
# b = int(input("Enter ending range of Required Tables: "))

# for i in range(a,b+1):
#     for x in range(1,11):
#         print(str(i)+" x "+str(x)+" = ", i*x)