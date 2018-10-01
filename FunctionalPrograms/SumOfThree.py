'''
*********************************************************************************************
 Purpose: Checks if the sum of 3 numbers is equal to zero or not

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   21-09-18


**********************************************************************************************
'''
try:
    number_array = list()
    number = int(input("How many elements do you want to enter"))
    print("Enter the elements")
    for i in range(number):
        n = int(input("Number:"))
        number_array.append(n)

    print("The triplets are")
    for j in range(number):
        for k in range(j+1, number):
            for l in range(k+1, number):
                if number_array[j]+number_array[k]+number_array[l] == 0:
                    print(number_array[j], number_array[k], number_array[l])

except Exception:
    print("Invalid input")
