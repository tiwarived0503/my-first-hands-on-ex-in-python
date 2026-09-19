#if-elif-else chain
age = 16
if age < 4:
    print('Your ammusement park fee is free')
elif 4 < age < 18:
    print('Your ammusement park fee is: 600Rs')
else:
    age > 18
    print('Your ammusement park fee is:900Rs')
# Instead of this you can write the same code as:
age = 16
if age < 4:
    price = 0
elif 4 < age < 18:
    price = 600
else:
    age > 18
    price = 900
print('Your fee for the ammusement park is: '+ str(price)+'Rs')

# using if statements with lists
lunch = ['roti','dal','rice','papad','pickle']
for items in lunch:
    if items == 'papad':
        print('Sorry yaar, i ate all the ' + items +"s")
    else:
        print('here it is ' + items)

# Checking That a List Is Not Empty
requested_topping = []
if requested_topping:
    for requested_toppings in requested_topping:
        print('Adding '+ requested_toppings +' into your pizza.')
else:
    print('Are you sure you want a plain pizza')