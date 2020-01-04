import json

student = {
    'Name':'Amjad',
    'Age': 25,
    'Class' :'AI'
}
# Methods = dump for write || load for read

#Exception Handling
try:
    print(10/0)
    with open('data.json','w') as fd:
        # json.dump(student, fd)
        student1 = json.load(fd)
        print(student1)
except FileNotFoundError:
    print('Please Check File Path. File not found in Specified Location.')
# except PermissionError:
#     print('')
except Exception as e:
    print(e)
    print('An un-known Exception Occured.')

print('I am still running.....')
print(student)