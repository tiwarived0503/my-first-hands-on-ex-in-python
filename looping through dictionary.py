# Looping Through All Key-Value Pair
user = {
    'first name':'ved',
    'last name':'tiwari',
    'username':'very_chalant_ved'
}
for key,value in user.items():
    print('\nkey: ' + key)
    print('value: ' + value)

people = {
    'ved':10,
    'lekh':7,
    'sonal':22,
    'amit':15,
    'payal':16
}
for name,number in people.items():
    print(name.title() + "'s fav number is " + str(number))

# Looping Through All the Keys in a Dictionary
people = {
    'ved':10,
    'lekh':7,
    'sonal':22,
    'amit':15,
    'payal':16
}
friends = ['ved','lekh']
for name in people:
    print(name.title())

    if name in friends:
        print('Hi ' + name.title() + ' you have got a special message')

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages:
     print('erin please take the poll')

# Looping Through a Dictionary’s Keys in Order
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name in sorted(favorite_languages):
    print('\n' + name.title() + ' ,Thanks for taking poll')

# Looping Through All Values in a Dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'pearl',
}
print('\n')
print('different langues are shown below')
for language in favorite_languages.values():
    print(language)

# .set() function removes the repitative statements
    favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print('\n')
for language in sorted(set(favorite_languages.values())):
    print(language)