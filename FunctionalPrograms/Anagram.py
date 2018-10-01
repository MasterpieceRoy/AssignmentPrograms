'''
*********************************************************************************************
 Purpose: Checks if entered elements are Anagram or Not

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   17-09-18


**********************************************************************************************
'''

def is_anagram(word1, word2):  # function definition
    if len(word1) != len(word2):  # check the length of both the alphabets
        print("The words cannot be anagram")
        exit(0)
    else:
        count1 = [0] * 256
        count2 = [0] * 256
        for i in word1:
            count1[ord(i)] += 1  # check the ascii value of the alphabet and stores the count
        for j in word2:
            count2[ord(j)] += 1  # check the ascii value of the alphabet and stores the count
    for i in range(256):
        if count1 == count2:  # checks if the count of both the characters are same or not
            print("The words are anagram to each other")
            break
    else:
            print("The words are not anagram to each other")


try:

    word1 = input(" Enter the first word ")
    word2 = input(" Enter the second word ")

    word1.upper()  # changes all the characters to upper case
    word2.upper()  # changes all the characters to upper case

    is_anagram(word1, word2)
except Exception:
    print("Invalid input detected")
# if res == 1:
#     print("Both the words are anagram ")
# else:
#     print(" The words entered are not anagram to each other ")
