f = open("Numbers.txt", "r")
number = f.read().split(" ")
for i in range(len(number)):
    num = int(number[i] % 11)
    number.append(number[num])
print(number)




