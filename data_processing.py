import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("All cities in Germany:")
temp1 = []
for i in cities:
    if i['country'] == 'Germany':
        temp1.append(i['city'])
print(temp1)
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
temp2 = []
for i in cities:
    if i['country'] == 'Spain':
        if float(i['temperature']) > 12:
            temp2.append(i['city'])
print(temp2)
print()

# Count the number of unique countries
print('The number of unique countries')
temp3 = []
for i in cities:
    temp3.append(i['country'])
print(len(set(temp3)))
print()


# Print the average temperature for all the cities in Germany
print('The average temperature for all the cities in Germany')
su = []
for i in cities:
    if i['country'] == 'Germany':
        su.append(i['temperature'])
tota = 0
for i in su:
    tota += float(i)
print(tota/len(su))
print()

# Print the max temperature for all the cities in Italy
print('The max temperature for all the cities in Italy')
temp4 = []
for i in cities:
    if i['country'] == 'Italy':
        temp4.append(i['temperature'])
print(max(temp4))