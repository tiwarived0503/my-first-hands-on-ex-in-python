motorcycles = ['honda','yamaha','suzuki','KTM','royal enfield']
print(motorcycles)
motorcycles[3] = 'harley davidson'
print(motorcycles)

motorcycles.append('BM bablu')
print(motorcycles)

motorcycles.insert(2, 'ducatti')
print(motorcycles)

del motorcycles[3]
print(motorcycles)

pop_motorcycle = motorcycles.pop()
print(pop_motorcycle)

pop_motorcycle = motorcycles.pop(3)
print(pop_motorcycle)

motorcycles.remove('yamaha')
print(motorcycles)