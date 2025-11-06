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

# Let's write a function to filter out only items that meet the condition
# Hint: condition will be associated with an anonymous function, e.x., lamdbda x: max(x)
def filter(condition, dict_list):
    temps = []
    for item in dict_list:
        if condition(item):
            temps.append(item)
    return temps

"""
filtered_list = filter(lambda x: x['country'] == ['Germany'], cities)
print(filtered_list)
"""

# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    temp = []
    for item in dict_list:
        temp.append(item[aggregation_key])
    return aggregation_function(temp)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temp1 = aggregate('temperature', lambda x: sum([float(i) for i in x]) / len(x), cities)
print(temp1)
print()

# Print all cities in Germany
print("All cities in Germany:")
temp2 = filter(lambda x: x['country'] == 'Germany', cities)
print([c['city'] for c in temp2])
print()

# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C:")
temp3 = filter(lambda x: x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
print([c['city'] for c in temp3])
print()

# Count the number of unique countries
print("The number of unique countries:")
temp4 = set([c['country'] for c in cities])
print(len(temp4))
print()


# Print the average temperature for all the cities in Germany
temp5 = aggregate('temperature',
                        lambda x: sum([float(i) for i in x]) / len(x),
                        filter(lambda x: x['country'] == 'Germany', cities))
print(temp5)
print()

# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy:")
temp6 = aggregate('temperature',
                      lambda x: max([float(i) for i in x]),
                      filter(lambda x: x['country'] == 'Italy', cities))
print(temp6)
print()