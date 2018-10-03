'''
*********************************************************************************************
 Purpose: Contains functions definitions of different programs which can be called and referred

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   24-09-18


**********************************************************************************************
'''

No_Of_Characters = 256  # total number of Character in ASCII table is 256


class Util:
    # function to check whether string is anagram or not
    @staticmethod
    def is_anagram(word1, word2):  # checks if entered characters are anagram or not
        count1 = 0
        count2 = 0
        if len(word1) != len(word2):
            print("Both the strings are not anagram ")
            exit()
        else:
            count1 = [0] * No_Of_Characters  # initialises the count1 array with the value of 0
            count2 = [0] * No_Of_Characters  # initialises the count2 array with the value of 0
            for i in word1:
                count1[ord(i)] += 1  # increment the value in count1 array for every character present
            for i in word2:
                count2[ord(i)] += 1  # increment the value in count1 array for every character present

        for i in range(No_Of_Characters):
            if count1[i] != count2[i]:  # checks if both the words has the same count
                print("The entered words are Not anagram")
                break
        else:
            print(" The entered words are Anagram")

    # function to generate prime numbers
    @staticmethod
    def isprime(number):
        lis = [0] * 1000
        position = 0
        for i in range(2, number + 1):
            isPrime = True
            for j in range(2, int(i/2+1)):  # iterates from 2 since 1 is not a prime number
                if i % j == 0:  # checks the remainder is equal to 0 or not
                    isPrime = False
                    break
            if isPrime:
                lis[position] = i  # if number is prime then inserts the number in the array
                position += 1
        return_array = [0] * position
        for k in range(0, position):
            return_array[k] = lis[k]
        return return_array

    # function to check if entered number is a palindrome number or not
    @staticmethod
    def ispalind(number):
        temp = number
        rev = 0
        while number != 0:  # iterates until the value of number is equal to zero
            new_num = number % 10  # calculates the modulus and stores it in new_num
            rev = rev * 10 + new_num  # starts multiplying in order to calculate the reverse
            number = number/10  # divides the number to shorten the number
        if rev == temp:  # checks if the new number is equal to the original number
            return True
        else:
            return False

    # function to swap the nibbles and calculate it's decimal equivalent
    @staticmethod
    def split8Bit(num):
        print("After swapping the nibbles decimal equivalent is ")
        return ((num & 0x0F) << 4 | (num & 0xF0) >> 4)  # swaps the nibbles and then returns it's decimal equivalent

    # function to check if the number that the user has in mind can be guessed or not
    @staticmethod
    def find_number(first, number):
        mid = int((first + number)/2)  # dividing the list of numbers into two halves
        if first < number:
            if first != mid:
                print("Is your number between ", str(first), " and ", str(mid), " ?")
            else:
                print("Is you number ", str(first))
            choice = input("Press y for yes and n for no")
            if choice == 'y':  # if the response is yes it means the number is below mid
                Util.find_number(first, mid)  # Recursively calls the find_number method
            elif choice == 'n':  # if the response is no it means the number is above mid
                Util.find_number(mid+1, number)  # Recursively calls the find_number method
            else:
                print("Invalid Input")
        elif first == number:
                print("The number is ", str(number))

    # function to calculate the Day of the week according to Eucledian calendar
    @staticmethod
    def dayofweek(month, day, year):
        # checks the entered month and converts it into respective month numerically
        if month == "January":
            month = 1
        elif month == "February":
            month = 2
        elif month == "March":
            month = 3
        elif month == "April":
            month = 4
        elif month == "May":
            month = 5
        elif month == "June":
            month = 6
        elif month == "July":
            month = 7
        elif month == "August":
            month = 8
        elif month == "September":
            month = 9
        elif month == "October":
            month = 10
        elif month == "November":
            month = 11
        elif month == "December":
            month = 12
        else:
            print("Invalid Month entered")
        # calculates the day of the month

        y0 = float((year - (14 - month)/12))
        x = float(y0 + (y0/4) - (y0/100) + (y0/400))
        m0 = float(month + 12 * ((14 - month)/12) - 2)
        d0 = int(day + x + (31 * m0)/12) % 7

        if d0 == 0:
            d0 = "Sunday"
            print(d0)
        elif d0 == 1:
            d0 = "Monday"
            print(d0)
        elif d0 == 2:
            d0 = "Tuesday"
            print(d0)
        elif d0 == 3:
            d0 = "Wednesday"
            print(d0)
        elif d0 == 4:
            d0 = "Thursday"
            print(d0)
        elif d0 == 5:
            d0 = "Friday"
            print(d0)
        elif d0 == 6:
            d0 = "Saturday"
            print(d0)

    # function to convert temperature from Celsius to Fahrenheit and vice-versa
    @staticmethod
    def temperaturconversion(choice, temp):
        if choice == 1:
            temp_in_fahren = float(temp * (9/5) + 32)  # calculates the temperature in Fahrenheit
            print("The temperature in Fahrenheit  is ", str(temp_in_fahren), "° F")
        else:
            temp_in_celsius = float((temp - 32) * 5/9)  # calculates the temperature in Celsius
            print("The temperature in Celsius  is ", str(temp_in_celsius), "° C")

    # function to calculate the monthly payment
    @staticmethod
    def monthlypayment(principle, year, rate):

        n = int(12 * year)  # calculates the total number of months
        r = float(rate / (12*100))  # calculates the rate of interest
        payment = float((principle * r)/(1 - (1 + r) ** (-n)))  # calculates the total monthly payment
        print("The total payment needed to be done per month is ", str(payment))


class Utility:

    # function to perform binary search
    @staticmethod
    def binary_search_number(key, lis):
        start = 0  # sets the pointer to first index
        end = len(lis) - 1  # sets the pointer to the last index
        while start <= end:  # checks until the pointer reaches the last index
            mid = int((start + end) / 2)  # points to the middle element in the list
            if key == lis[mid]:  # checks if the entered element is present in the middle of the list itself
                print("\nEntered search is present at position:", mid)
                return -1
            elif key < lis[mid]:  # checks if the entered number to be searched is below the value at middle of the lis
                end = mid - 1
            elif key > lis[mid]:  # checks if the entered number to be searched is greater the value at middle of lis
                start = mid + 1  # if true increments the start pointer
        print("\nElement not found!")
        return -1

    # function to search the word in the entered list
    @staticmethod
    def binary_search_word(lis, word):
        start = 0
        end = len(lis) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if word == lis[mid]:
                print("\nEntered number is present at position:", mid)
                return -1
            elif word < lis[mid]:
                end = mid - 1
            elif word > lis[mid]:
                start = mid + 1
        print("\nElement not found!")
        return -1

    # function to sort the array of numbers using insertion sort algorithm
    @staticmethod
    def insertion_sort_number(lis):
        for i in range(1, len(lis)):

            key = lis[i]  # stores the first number in the temporary variable key

            j = i - 1
            while j >= 0 and key < lis[j]:  # iterates until the value of j is greater than 0
                lis[j + 1] = lis[j]  # arranges the next number i.e. swaps
                j -= 1  # decrements the value of j if the number is found
            lis[j + 1] = key  # swaps the value previously stored in the temp variable key to the previous position
        return lis  # returns the sorted list

    # function to sort the array of words using insertion sort algorithm
    @staticmethod
    def insertion_sort_string(lis):
        for i in lis:  # iterate for every word in the list
            j = lis.index(i)
            while j > 0:  # loops until it reaches the end of the list
                if lis[j - 1] > lis[j]:
                    lis[j - 1], lis[j] = lis[j], lis[j - 1]  # swaps the alphabets
                else:

                    break
                j = j - 1
        return lis

    # function to sort the list of numbers using bubble sort algorithm
    @staticmethod
    def bubble_sort_number(lis):
        for i in range(len(lis)):  # iterates for every number in the list
            for j in range(0, len(lis) - i - 1):  # loops until the element present in first index to last index
                if lis[j] > lis[j + 1]:

                    # swaps the elements
                    temp = lis[j]
                    lis[j] = lis[j + 1]
                    lis[j + 1] = temp
        return lis

    # function to sort the list of numbers using bubble sort algorithm
    @staticmethod
    def bubble_sort_string(lis):
        for i in range(len(lis) - 1, 0, -1):  # iterates for every character in the list
            for j in range(i):
                if lis[j] > lis[j + 1]:  # loops until the character present in first index to last index

                    # swaps the characters
                    temp = lis[j]
                    lis[j] = lis[j + 1]
                    lis[j + 1] = temp
        return lis


# function to sort the list of numbers using merge sort algorithm
def mergesort(lis, lo, hi):

    mid = int(lo + (hi - lo) / 2)  # function to calculate the middle index

    if lo < hi:
        mergesort(lis, lo, mid)  # recursively calls the merge sort and further splits the left array
        mergesort(lis, mid + 1, hi)  # recursively calls the merge sort and further splits the right array
        merge(lis, lo, mid, hi)  # recursively calls the merge function where merging takes place


def merge(lis, lo, mid, hi):  # function to merge both the arrays i.e the left and the right array
    n1 = int(mid - lo + 1)  # pointer for left side of the array
    n2 = hi - mid   # pointer for right side of the array

    left_array = [0] * n1  # initialises all the indexes with the value 0
    right_array = [0] * n2  # initialises all the indexes with the value 0

    for i in range(0, n1):
        left_array[i] = lis[lo + i]

    for j in range(0, n2):
        right_array[j] = lis[mid + 1 + j]

    i = 0  # Initial index of first array
    j = 0  # Initial index of second array
    k = lo  # Initial index of merged array

    # Merge the temp arrays back into array
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            lis[k] = left_array[i]
            i = i + 1
        else:
            lis[k] = right_array[j]
            j = j + 1
        k = k + 1

    # Insert the remaining elements of left_array
    while i < n1:
        lis[k] = left_array[i]
        i = i + 1
        k = k + 1

    # Insert the remaining elements of right_array
    while j < n2:
        lis[k] = right_array[j]
        j = j + 1
        k = k + 1


# function to convert the number from decimal to binary
def to_binary(number):
    bin_num = 0
    power = 0
    while number > 0:  # iterates until the number becomes zero
        bin_num += 10 ** power * (number % 2)  # using the power of 10 since binary is to the base 10
        number //= 2  # divides the number by 2 and returns the floor value
        power += 1  # increments the power value
    return bin_num
