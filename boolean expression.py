#if statements
cars = ['audi' , 'bmw','mercedes','toyota']
for car in cars:
    if car == cars[1]:
        print(car.upper())
    else:
        print(car.title())

#conditional tests
car = 'bmw'
print(car == 'bmw')

car = 'audi'
print(car == 'bmw')

car = 'audi'
print(car == 'Audi')

carar = 'Audi'
print(car.lower() == 'audi')

#checking for inequality
fav_toppings = 'olive seeds'
if fav_toppings != 'mushrooms':
    print('i dont want that')

#Numerical Comparisons
age = 18
print(age == 18)

age = 18
if age != 27:
    print('you are underated')

age = 18
print(age < 18)

age = 18
print(age <= 18)

age = 18
print(age > 18)

age = 18
print(age >= 18)

#Checking Multiple conditions
age_A = 18
age_B = 19
print(age_A >15 and age_B>20)

age_A = 18
age_B = 19
print(age_A >15 or age_B>20)

# Checking Whether a Value Is in a List
fav_topping = ['olive seeds','chilly flecks','mushrooms','origano']
if "origano" in  fav_topping:
    print('i can take that pizza')

banned_users = ['munna', 'circuit', 'shyam', 'raju']
user = 'babu rao'
if user not in banned_users:
    print('You can enter the comedy show')
    