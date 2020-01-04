# def adder(num1, num2):
#     def add():
#         return num1+num2
#     return add()
# print(adder(3,4))

def populate(my_list):
    def actual_populate():
        for i in range(0,11):
            my_list.append(i)
    actual_populate()
ml=[]
populate(ml)
print(ml)