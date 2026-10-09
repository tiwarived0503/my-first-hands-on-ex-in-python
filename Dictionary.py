# A simple dictionary
lekh = {'food':'maggi masala','game':"bomb squad"}
print(lekh['food'])
print(lekh['game'])

# Adding New Key-Value Pairs
lekh['surname'] = 'tiwari'
lekh['fav ipl team'] = 'Chennai Super Kings'
lekh['height'] = '142cm'
print(lekh)

# Modifying Values in a Dictionary
jaadu = {'color':'blue','food source':'sunglight'}
jaadu['color'] = 'ocean blue'
print(jaadu)

# Removing Key-Value Pairs
jaadu = {'color':'blue','food source':'sunglight'}
del jaadu['color']
print(jaadu)

# A Dictionary of Similar Objects
fav_langs = {
    'ved':'python',
    'lekh':'gaali',
    'sonal':'scolding',
}
print(fav_langs)
print(fav_langs['ved'].title() + " is the favourite language of ved")