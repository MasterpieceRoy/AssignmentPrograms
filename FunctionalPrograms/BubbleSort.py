def bubble_sort(numbers_array):
    for i in range(len(numbers_array)-1,0,-1):
        for j in range(i):
            if numbers_array[j]>numbers_array[j+1]:
                temp = numbers_array[j]
                numbers_array[j] = numbers_array[j+1]
                numbers_array[j+1] = temp
    return numbers_array


numbers_array = list()
n = int(input("Enter the number of elements"))
print("Enter the elements")
for i in range(0, n):
    n = input()
    numbers_array.append(n)

sorted_array = bubble_sort(numbers_array)
print(sorted_array)
