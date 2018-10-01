print("Hello \n")
size = int(input("Enter a range"))
low = 0
high = size
while True:
    mid = int((low+high)/2)
    print("Is your number ", mid)
    choice = input("Enter yes or higher or lower:\t \n")
    if choice == "yes":
        print("Number found at ", str(mid))
        break
    elif choice == "lower":
        high = mid-1
    else:
        low = mid+1
