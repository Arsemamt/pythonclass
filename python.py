name = 'asdf'
print(name.count('a'))

adsf = True  # has to be capital

students_list = ['hanna', 'john']
students_list[1] = 'adfd'
print(type(students_list))
print(students_list[1])
print(students_list)

# tuple
names = ('hanna', 'kaasd')

students_list.append('haliu')
students_list.insert(1, 'asdu')

# set
student_info = {'name': 'amlk',
                'age': 34,
                'sec': 'b',
                'height': 1.4,
                'skills': ['c', 'd']
                }

# control state
for value in range(0, 12):
    # pass - if you don't want to declare it
    print(value)

for value in students_list:
    print(value)

for index, value in enumerate(students_list):
    print(index, value)

age = 45
if age > 18:
    print('adult')

elif age < 18: 
    print('under age ')

else:
    print('error')


def greet():
    print('hi world ')

def greet_with_name(name):
    print(f'hello: {name}')


greet()
greet_with_name('hanna')




def greet_with_name(name,age, lastName = 'kebede'):
    print(f'hello: {name} age: {age} last Name: {lastName}')


greet()
greet_with_name(name='hanna',age =12)


def greet_with_name(*numbers):
    print(numbers)
    print(f'hello {name}')

greet_with_name('hanna', 'kebede')