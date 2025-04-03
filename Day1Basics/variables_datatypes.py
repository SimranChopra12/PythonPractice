# Variables in Python
first_name = 'Sim'
last_name = 'Chopra'
country = 'Can'
city = 'Hfx'
age = 250

# Generate and print the pattern
for n in range(1, 6):
    print(n, 1, n, n**2, n**3)

skills = ['HTML', 'CSS', 'JS', 'React', 'Python']

#use int() to
side_a = int(input('What is your side a?'))
print(type(side_a))
side_b = int(input('What is your side b?'))
side_c = int(input('What is your side c?'))
print(type(side_a))
perimeter = side_a + side_b + side_c
print(perimeter)

print(first_name, last_name, country, age)

#declaring multiple variables in one line
first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)


#getting input from user

name = input("what is your name?")

print(name)

#check data type using type()
print(type(name))

print ('Division: ', 4 / 2)       # 2.0  Division in Python gives floating number
print('Division without the remainder: ', 7 // 2)   # 3,  gives without the floating number or without the remaining
print ('Division without the remainder: ',7 // 3)   # 2