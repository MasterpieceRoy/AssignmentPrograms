import json
from Patient import *
from Doctor import *

def add_doc():
    doc_obj = Doctor()
    data = {}
    data["doctor"] = {}
    data = json.load("Doctor.json", "r")
    try:
        f_name = input("Enter the First Name")
        doc_obj.set_first_name(f_name)

        l_name = input("Enter the Last Name")
        doc_obj.set_last_name(l_name)

        id = input("Enter id")
        if len(id) > 4:
            print("Invalid Id")
            exit(0)
        else:
            doc_obj.set_id(id)

        specialization = input("Enter Specialization ")
        doc_obj.set_specialization(specialization)

        avail = input("Enter availability")
        doc_obj.set_availability(avail)






def add_pat():
    pat_obj = Patient()
    data = {}
    data["patient"] = {}
    data = json.load("Patient.json", "r")
    try:
        f_name = input("Enter the First Name")
        pat_obj.set_first_name(f_name)

        l_name = input("Enter the Last Name")
        pat_obj.set_last_name(l_name)

        id = input("Enter id")
        if len(id) > 6:
            print("Invalid Id")
            exit(0)
        else:
            pat_obj.set_id(id)

        mob_number = input("Enter the Mobile number ")
        if len(mob_number) > 10:
            print("Invalid Mobile number !!!! Please try again")
        else:
            pat_obj.set_mob_number(mob_number)



def search_doc():
    pass


def search_pat():
    pass


def book_apt():
    pass


class Clinic:
    while 1:

        print("""
        Select a choice:-
        1. Add a Doctor
        2. Add a Patient
        3. Search for a Doctor by name, id, Specialization or Availability
        4. Search for a Patient by name, mobile number or id
        5. Book an Appointment
        6. Exit
        
        """)
        choice = int(input())
        if choice == 1:
            add_doc()
        elif choice == 2:
            add_pat()
        elif choice == 3:
            search_doc()
        elif choice == 4:
            search_pat()
        elif choice == 5:
            book_apt()
        elif choice == 6:
            print("\t \t \t Dhanyawad")
            exit(0)
        else:
            print("Invalid Input")
