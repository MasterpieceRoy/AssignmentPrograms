'''
*********************************************************************************************
 Purpose: Generates n number of distinct coupons

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   18-09-18


**********************************************************************************************
'''
import random

try:

    number = int(input("How many coupons do you need"))
    count = 0
    i = 0
    random_array = [""]
    while True:
            count += 1
            ran = int(random.randint(1, number*2))  # generates random number double to the size of the input
            for i in range(len(random_array)):
                if random_array[i] == ran:  # checks if the number generated is same or not
                    break
                else:
                    if i == len(random_array)-1:
                        random_array.append(ran)  # adds the number to the random_array array

            if len(random_array) == number+1:
                break

    print("The number of coupons required to ", str(count))
except Exception:
    print("Invalid Input detected")
