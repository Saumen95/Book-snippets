coordinates = (33.566, 65.667)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
travel_id = [('USA', '31195855'), ('BRA', 'CE342567'),
             ...
             ('ESP', 'XDA205856')]
for passport in sorted(travel_id):
    print('%s %s' % passport)

for country, _ in travel_id:
    print(country)
