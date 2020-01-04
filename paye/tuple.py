tuple1=(1,"new",2,3,4,"new") 
# Tuples are immutable i.e. values once assigned cannot 
# be changed(deleted, removed, popped or appended).
# print(tuple1) 
# print(tuple1[1]) #indexing
# print(tuple1[1:4]) #slicing
# print(tuple1.index("new")) #Index method: Brings index of given value in tuple
# print(tuple1.count("new")) #Count method: Counts the instances of given value in a tuple

for i in tuple1:
    if i=="new":
        print(tuple1.index(i))

        #Do it at home