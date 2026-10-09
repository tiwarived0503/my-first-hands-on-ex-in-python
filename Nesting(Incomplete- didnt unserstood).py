# Nesting
aliens = []
for alien_number in range(0,31):
    alien = {'color':'green','points':5,'speed':'medium'}
    aliens.append(alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] == 'blue'
        alien['points'] == 100
        alien['speed'] == 'slow'
for alien in aliens:
    print(alien)
