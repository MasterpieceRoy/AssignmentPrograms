Celsius = [45, 39.2, 37.8]
Fahrenheit = list(map(lambda x: (float(9)/5)*x + 32, Celsius))
print(Fahrenheit)

sum = [20, 40, 60, 80]


from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)
