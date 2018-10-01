'''
*********************************************************************************************
 Purpose: Searches the entered word in the file with the help of Binary Search Algorithm

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   27-09-18


**********************************************************************************************
'''
from Util import *  # imports all the function definitions from Util package

try:
    input_file = input("Enter File name : ")
    file_txt = open(input_file)  # default it will open in read mode
    text = file_txt.read()  # to read file-object

    space = 0
    line = 0
    char = 0

    for i in text:
        # reading text character by character
        if i == " ":
            space += 1
        elif i == "\n":
            line += 1
        else:
            char += 1
    totalcharcs = space + line + char
    content_list = []
    with open(input_file) as f:
        # Content_list is the list that contains the read lines.
        rd = f.read()
        content_list = rd.split(" ")  # splits the word separated with spaces
        print(content_list)
    key = input("Enter the word that you want to search ")
    Utility.binary_search_word(content_list, key)  # calls the binary_search function

except FileNotFoundError:
    print("File not Found")
except ValueError:
    print("Invalid input")
