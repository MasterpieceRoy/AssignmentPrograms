'''
*********************************************************************************************
 Purpose: Finds out the best possible way in which the deadlines can be achieved

 *  @author  Abhishek Roy
 *  @version 1.0
 *  @since   29-09-18


**********************************************************************************************
'''

try:
    count = int(input("Enter the number of Tasks"))
    deadlinelis = [0] * count  # initializes the entire deadline array with the value of 0
    timelis = [0] * count  # initializes the entire deadline array with the value of 0

    for i in range(count):
        print("Enter deadline and time required for the task number :" + str(i + 1) + " ")
        deadlinelis[i] = input()  # inputs the deadlines
        timelis[i] = input()  # inputs the total time required to complete the tasks
    for i in range(1, len(deadlinelis)):
        deadlineKey = deadlinelis[i]  # stores the first deadline in the temporary variable called deadlineKey
        timeKey = timelis[i]  # stores the first time in the temporary variable called timeKey
        j = i - 1
        while (j > -1) and (deadlinelis[j] > deadlineKey):  # compares the last and the previous element
            deadlinelis[j + 1] = deadlinelis[j]  # swaps the first and the next deadline
            timelis[j + 1] = timelis[j]  # swaps the last and it's previous time
            j -= 1
        deadlinelis[j + 1] = deadlineKey  # stores the deadline in the new index
        timelis[j + 1] = timeKey  # stores the time in the new index

    for i in range(count):  # used to print the entered deadline and time
        print("The entered deadline and time required for the task number :" + str(i+1) + " ", end='')
        print(str(deadlinelis[i]) + "\t", end='')
        print(str(timelis[i]))

    for i in range(count):  # used to calculate the tasks
        print("Task " + str(i+1) + ":" + str(timelis[i]))

except Exception:
    print("Invalid input")



