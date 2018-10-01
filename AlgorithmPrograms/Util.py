'''
*********************************************************************************************
 Purpose: Contains functions definitions of different programs which can be called and referred

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   24-09-18


**********************************************************************************************
'''

# function to check whether string is anagram or not

No_Of_Characters = 256  # total number of Character in ASCII table is 256


class Util:

    @staticmethod
    def is_anagram(word1, word2):  # checks if entered characters are anagram or not
        count1 = 0
        count2 = 0
        if len(word1) != len(word2):
            print("Both the strings are not anagram ")
            exit()
        else:
            count1 = [0] * No_Of_Characters
            count2 = [0] * No_Of_Characters
            for i in word1:
                count1[ord(i)] += 1
            for i in word2:
                count2[ord(i)] += 1

        for i in range(No_Of_Characters):
            if count1[i] != count2[i]:
                print("The entered words are Not anagram")
                break
        else:
            print(" The entered words are Anagram")

    @staticmethod
    def split8Bit(num):
        print("After swapping the nibbles decimal equivalent is ")
        return ((num & 0x0F) << 4 | (num & 0xF0) >> 4)




    @staticmethod
    def isprime(number):
        lis = [0] * 1000
        position = 0
        for i in range(2, number + 1):
            isPrime = True
            for j in range(2, int(i/2+1)):
                if i % j == 0:
                    isPrime = False
                    break
            if isPrime:
                lis[position] = i
                position += 1
        return_array = [0] * position
        for k in range(0, position):
            return_array[k] = lis[k]
        return return_array

    @staticmethod
    def ispalind(number):
        if len(number) < 2:
            return False

        array = []
        n = len(array)
        for i in range(n):
            if array[i] != array[n - 1 - i]:
                return False
        return True


    @staticmethod
    def find_number(first, number):
        mid = int((first + number)/2)
        if first < number:
            print("Is your number between ", str(first), " and ", str(mid), " ?")
            choice = input("Press y for yes and n for no")
            if choice == 'y':
                Util.find_number(first, mid)
            else:
                Util.find_number(mid+1, number)
        elif first == number:
             print("The number is ", str(number))

    @staticmethod
    def dayofweek(month, day, year):
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



    @staticmethod
    def temperaturconversion(choice, temp):
        if choice == 1:
            temp_in_fahren = float(temp * (9/5) + 32)
            print("The temperature in Fahrenheit  is ", str(temp_in_fahren), "° F")
        else:
            temp_in_celsius = float((temp - 32) * 5/9)
            print("The temperature in Celsius  is ", str(temp_in_celsius), "° C")

    @staticmethod
    def monthlypayment(principle, year, rate):

        n = int(12 * year)
        r = float(rate / (12*100))
        payment = float((principle * r)/(1 - (1 + r) ** (-n)))
        print("The total payment needed to be done per month is ", str(payment))


class Utility:
    # notes = [20, 22, 23, 24]
    @staticmethod
    def binary_search_number(key, lis):
        # print(Utility.notes)
        start = 0
        end = len(lis) - 1
        while start <= end:
            mid = int((start + end) / 2)
            if key == lis[mid]:
                print("\nEntered search is present at position:", mid)
                return -1
            elif key < lis[mid]:
                end = mid - 1
            elif key > lis[mid]:
                start = mid + 1
        print("\nElement not found!")
        return -1

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

    @staticmethod
    def insertion_sort_number(lis):
        for i in range(1, len(lis)):

            key = lis[i]

            j = i - 1
            while j >= 0 and key < lis[j]:
                lis[j + 1] = lis[j]
                j -= 1
            lis[j + 1] = key
        return lis

    @staticmethod
    def insertion_sort_string(lis):
        for i in lis:
            j = lis.index(i)
            while j > 0:
                if lis[j - 1] > lis[j]:
                    lis[j - 1], lis[j] = lis[j], lis[j - 1]
                else:

                    break
                j = j - 1
        return lis

    @staticmethod
    def bubble_sort_number(lis):
        for i in range(len(lis)):
            for j in range(0, len(lis) - i - 1):
                if lis[j] > lis[j + 1]:
                    temp = lis[j]
                    lis[j] = lis[j + 1]
                    lis[j + 1] = temp
        return lis

    @staticmethod
    def bubble_sort_string(lis):
        for i in range(len(lis) - 1, 0, -1):
            for j in range(i):
                if lis[j] > lis[j + 1]:
                    temp = lis[j]
                    lis[j] = lis[j + 1]
                    lis[j + 1] = temp
        return lis






def mergesort(lis, lo, hi):

    mid = int(lo + (hi - lo) / 2)

    if lo < hi:
        mergesort(lis, lo, mid)
        mergesort(lis, mid + 1, hi)
        merge(lis, lo, mid, hi)


def merge(lis, lo, mid, hi):
    n1 = int(mid - lo + 1)
    n2 = hi - mid

    left_array = [0] * n1
    right_array = [0] * n2

    for i in range(0, n1):
        left_array[i] = lis[lo + i]

    for j in range(0, n2):
        right_array[j] = lis[mid + 1 + j]

    # Merge the temp arrays back into array
    i = 0  # Initial index of first array
    j = 0  # Initial index of second array
    k = lo  # Initial index of merged array

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


def to_binary(number):
    bin_num = 0
    power = 0
    while number > 0:
        bin_num += 10 ** power * (number % 2)
        number //= 2
        power += 1
    return bin_num



