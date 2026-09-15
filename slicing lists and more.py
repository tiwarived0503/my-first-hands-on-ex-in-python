#slicing
players = ['Ved','lekh','sonal','amit','satish','nirmala']
print(players[1:5])
print(players[:3])
print(players[3:])
print(players[-3:])

#looping throught a slice
family = ['Ved','lekh','sonal','amit','satish','nirmala']
for people in family[:4]:
    print(people)

#copying a list 
hall_item = ['chair','sofa','tv','remote']
bedroom_item = hall_item[:]
bedroom_item.append('bed')
hall_item.append('family photo')
print(hall_item)
print(bedroom_item) 