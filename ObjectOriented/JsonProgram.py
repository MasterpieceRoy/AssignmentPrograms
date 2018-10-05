import json

rice = '{ "name":"Basmati", "price":81, "Weight":2 }'
pulses = '{ "name":"Urad", "price":62, "Weight":3 }'
wheats = '{ "name":"Brown", "price":22, "Weight":4 }'
x = json.loads(rice)
y = json.loads(pulses)
z = json.loads(wheats)


# the result is a Python dictionary:
print(x["name"], end=" Costs Rs.")
print(x["price"]*x["Weight"])

print(y["name"], end=" Costs Rs.")
print(y["price"]*y["Weight"])

print(z["name"], end=" Costs Rs.")
print(z["price"]*z["Weight"])
