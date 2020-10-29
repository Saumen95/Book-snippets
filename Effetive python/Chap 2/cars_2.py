car_inventory = {
'Downtown': ('Silver Shadow', 'Pinto', 'DMC'),
'Airport': ('Skyline', 'Viper', 'Gremlin', 'Nova'),
}

((loc1, (best1,*rest1)),
(loc2, (best2,*rest2))) = car_inventory.items()
print(f'best at {loc1} is {best1}, {len(rest1)} others')
print(f'best at {loc2} is {best2}, {len(rest2)} others')
