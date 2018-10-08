import json

data = json.load(open("Inventorydata.json", "r"))

def inventory_detail(inventory_name):
    print("enter the ", inventory_name, "detail..")
    print("Enter the name:")
    name = input()
    print("Enter the price:")
    price = int(input())
    print("Enter how many kg.?")
    kg = int(input())
    print("The total amount to pay")
    amount = int(price * kg)

    obj = Inventory(name, price, kg, amount, inventory_name)
    obj.maintain()

class Inventory:
    def __init__(self, name , price , kg, amount, inventory_name):
        self.name = name
        self.price = price
        self.kg = kg
        self.amount = amount
        self.inventory_name = inventory_name

    def maintain(self):
        data["inventory"][self.inventory_name].append({
            "Name": self.name,
            "Price": self.price,
            "Kg": self.kg,
            "amount": self.amount
        })

        print("Name ", self.name)
        print("Price ", self.price)
        print("Kg  ", self.kg)
        print("Total amount ", self.amount)

        with open("Inventorydata.json", "w") as inventory_data:
            json.dump(data, inventory_data, sort_keys=True)

class DataManagement:
    while True:
        print("Enter your Choice")
        print("Enter 1 for Rice")
        print("Enter 2 for pulses")
        print("Enter 3 for wheat")
        print("Enter 4 to Save and Exit")
        choice = int(input())

        if choice == 1:
            name = "rice"
            inventory_detail(name)

        elif choice == 2:
            name = "pulses"
            inventory_detail(name)
        elif choice == 3:
            name = "wheat"
            inventory_detail(name)
        elif choice == 4:
            print("Data saved successfully")
            exit(0)
        else:
            print("Invalid choice")