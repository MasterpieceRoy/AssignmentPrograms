from LinkedListOfQueue import *
class PrimeAnagramUsingQueue:

    # Function to find Anagram number
    # @param str1
    # @param str2
    def isAnagram(str1, str2):
        if sorted(str1) == sorted(str2):
            return True
        else:
            return False

    obj = LinkedListOfQueue()
    number = int(input("enter the range between 1 to 1000\n"))
    arr = []
    i = 2
    while i < number:
        j = 2
        flag = 0
        while j < i:
            if i % j == 0:
                flag = 1
            j += 1
        if flag == 0:
            arr.append(str(i))
        i += 1

    i = 0
    while i < len(arr):
        j = i + 1
        while j < len(arr):
            if isAnagram(arr[i], arr[j]):
                obj.enque(arr[i])
                obj.enque(arr[j])
            j += 1
        i += 1
    obj.display()