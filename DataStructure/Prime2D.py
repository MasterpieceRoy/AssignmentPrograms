class PrimeTwoDList:

    # Function to initialize a constructor
    # param rang
    def __init__(self, rang):
        number = 0
        twoDRange = range(0, 10)

        twoDRange = ['0-100', '101-200', '201-300', '301-400', '401-500', '501-600', '601-700', '701-300', '801-900',
                     '900-1000']
        new_array = []
        rang = int(rang/100)
        for twoDArray in range(0, rang):
            temp = []
            for num in range( number, number+100):
                if num > 2:
                    for k in range(2, num):
                        if num % k == 0:
                            flag = 0
                            break
                        else:
                            flag = 1
                    if flag == 1:
                        temp.append(num)
                else:
                    pass
            number = number + 100
            temp1 = [twoDRange[twoDArray], temp]
            new_array.append(temp1)
        print(new_array)


if __name__ == '__main__':
    while 1:
        try:
            userNumber = int(input("enter the number between 1 to 1000"))
            PrimeTwoDList(userNumber)
            exit(0)
        except IndexError:
            print("index error")

        except ValueError:
            print('value error')
        except NameError:
            print("name error")
        except OverflowError:
            print("OverflowError")
        except SyntaxError:
            print("SyntaxError")
