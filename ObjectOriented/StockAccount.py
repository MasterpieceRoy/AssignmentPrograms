
from DetailData import *


class StockAccount:
    data = DetailData()
    while True:
        print("-----------Stock Accounts-----------")
        print("enter 1.To add a Customer")
        print("enter 2.To add a Company")
        print("enter 3.To display Customer")
        print("enter 4.To display Company")
        print("enter 5.For Transaction")
        print("enter 6.For Exit")

        choice = int(input("\nEnter your choice"))

        if choice == 1:
            data.add_customer()
        elif choice == 2:
            data.add_company()
        elif choice == 3:
            print("---------Total Customer--------")
            data.display_customer()
        elif choice == 4:
            data.display_company()
        elif choice == 5:
            data.transaction()
        elif choice == 6:
            exit(0)
        else:
            print("Invalid choice !!! Please Try again")
