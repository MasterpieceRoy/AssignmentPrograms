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
    deadlinelis = [0] * count
    timelis = [0] * count

    for i in range(count):
        print("Enter deadline and time required for the task number :" + str(i + 1) + " ")
        deadlinelis[i] = input()  # inputs the deadlines
        timelis[i] = input()  # inputs the total time required to complete the tasks
    for i in range(1, len(deadlinelis)):
        deadlineKey = deadlinelis[i]  # stores the
        timeKey = timelis[i]
        j = i - 1
        while (j > -1) and (deadlinelis[j] > deadlineKey):
            deadlinelis[j + 1] = deadlinelis[j]
            timelis[j + 1] = timelis[j]
            j -= 1
        deadlinelis[j + 1] = deadlineKey
        timelis[j + 1] = timeKey
    for i in range(count):
        print("The entered deadline and time required for the task number :" + str(i+1) + " ", end='')
        print(str(deadlinelis[i]) + "\t", end='')
        print(str(timelis[i]))
    for i in range(count):
        print("Task " + str(i+1) + ":" + str(timelis[i]))

except Exception:
    print("Invalid input")



