try:
    lis = []
    size = int(input("Enter the size of the list"))
    print("Enter the elements")
    for i in range(size):
        number = input("Enter number")
        lis.append(number)

    for i in lis:
        j = lis.index(i)
        while j > 0:
            if lis[j-1] > lis[j]:
                lis[j-1], lis[j] = lis[j], lis[j-1]
            else:

                break
            j = j-1
    print(lis)
except Exception:
    print("Invalid input detected")