print("Hi, my name is Hardik")
name = input("What is your name? ")
sum = ""
for i in name:
    sum = i + sum

print(sum,",OLLEH")
print("My favourite pet is a dog")
print('''
here's a picture of a dog:
o____
 ||||
 ''')
num = int(input("What is your favourite number?: "))
if num == 88 or num == 8: 
    print("Same!")
else:
    print("Ok")
age = int(input("What year were you born?: "))
age = 2025 - age
print("You are {0} years old".format(age))
age = age + 10
print("You will be {0} years old in 2035!".format(age))
age = age - 10
dog_year = age * 7
print("Your age is dog years would be {0}!".format(dog_year))
print('ha ' * 4)
print('ba' + 'na' *2)
print('Hello' + '!' *10)

print('Here is a scarf:')
print('~#' * 10)
print('#-' * 10)
print('Here is a wave:')
print('/\  ' * 10)