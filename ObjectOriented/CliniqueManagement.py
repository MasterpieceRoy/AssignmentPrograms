import json
from Patient import *
from Doctor import *
from datetime import *
from Appointment import *


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

        data["doctor"][f_name] = ({
            'f_name': doc_obj.get_first_name(),
            'l_name': doc_obj.get_last_name(),
            'id' : doc_obj.get_id(),
            'specialization': doc_obj.get_specialization(),
            'avail': doc_obj.get_availability()
        })
        with open('Doctor.json', 'w') as database1:
            json.dump(data, database1, sort_keys="True")
        print("Doctor Detail Added Successfully")

    except (NameError, SyntaxError, TypeError):
        print("Not a proper type of data")


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
        data["patient"][f_name] = ({
            'f_name': pat_obj.get_first_name(),
            'l_name': pat_obj.get_last_name(),
            'id': pat_obj.get_id(),
            'mobile': pat_obj.get_mob_number()
        })
        with open('Patient.json', 'w') as database1:
            json.dump(data, database1, sort_keys="True")
        print("Patient Detail Added Successfully")

    except (NameError, SyntaxError, TypeError):
        print("Not a proper type of data")


def book_apt():
    doctor_name = input("Enter the name of the doctor you want to book an appointment with")
    doc_avail = search_doc_name(doctor_name)
    count = 0

    if doc_avail is not None:
        appointment_list = json.load('Appointment.json', 'r')
        appointment = appointment_list["appointment"]
        for data in appointment:
            if doc_avail['f_name'] == data["doctor"]["f_name"]:
                count += 1
            print("Dr. ", doc_avail['f_name'], " has ", count, " appointments")
            if count < 5:
                pat_name = input("Enter the name of the patient that you want to search")
                pat_avail = search_pat_name(pat_name)

                if pat_avail is not None:
                    print("Doctor will be available")
                    print(add_appointment_details(doc_avail, pat_avail))
                else:
                    print("Patient not found")

            else:
                print("Doctor will not be available")


def add_appointment_details(doc_avail, pat_avail):
    data = json.load("Appointment.json", "r")

    doctor_obj = Doctor()
    patient_obj = Patient()

    appointment_doctor = Appointment()

    appointment_doctor.set_doctor(doc_avail)

    appointment_doctor.set_patient(pat_avail)

    now = datetime.now()

    appointment_doctor.set_date(str(now)[:10])

    try:
        data["appointment"].append(
            {
                'doctor': appointment_doctor.get_doctor(),'patient':appointment_doctor.get_patient(),
                'date': appointment_doctor.get_date()
            }
        )
        with open('Appointment.json', 'w') as database1:
            json.dump(data, database1, sort_keys= True)
        print("Details added successfully")

    except Exception:
        print("Data is not proper")


def search_doc():
    name_check = input("Enter the Name of the Doctor or Id or Specialization or Availability")
    try:
        list_doctor = json.load("Doctor.json", "r")
        name_keys = list(list_doctor["doctor"].keys())
        for data in name_keys:
            if list_doctor["doctor"][data]["f_name"] == name_check or list_doctor["doctor"][data]["id"] == name_check or list_doctor["doctor"][data]["specialization"] == name_check or list_doctor["doctor"][data]["avail"] == name_check:
                print("\t ID \t First Name \t Last Name \t Specialization \t Availability")
                print("\t", list_doctor["doctor"][data]["id"], "\t", list_doctor["doctor"][data]["f_name"], " ", ["l_name"], "\t", list_doctor["doctor"][data]["specialization"], "\t", list_doctor["doctor"][data]["avail"])

    except SyntaxError:
        print("Improper Input")


def search_pat():
    name_check = input("Enter the Name of the Patient or mobile number or id")
    try:
        list_pat = json.load("Patient.json", "r")
        name_keys = list(list_pat["patient"].keys())
        for data in name_keys:
            if list_pat["patient"][data]["f_name"] == name_check or list_pat["patient"][data]["id"] == name_check or list_pat["patient"][data]["mob_number"] == name_check:
                print("\t ID \t First Name \t Last Name \t Mobile \t")
                print("\t", list_pat["patient"][data]["id"], "\t", list_pat["patient"][data]["f_name"], " ",
                      ["l_name"], "\t", list_pat["patient"][data]["mob_number"])

    except SyntaxError:
        print("Improper Input")


def search_doc_name(doctor_name):
    count = 0
    try:
        doctor_lis = json.load("Doctor.json", "r")
        name_keys = list(doctor_lis["doctor"].keys())
        for data in name_keys:
            if doctor_lis["doctor"][data]["f_name"] == doctor_name or doctor_lis["doctor"][data]["id"] == doctor_name or doctor_lis["doctor"][data]["specialization"] == doctor_name:
                count += 1
                doctid = doctor_lis["doctor"][data]["id"]
                doctfname = doctor_lis["doctor"][data]["f_name"]
                doctlname = doctor_lis["doctor"][data]["l_name"]
                doctspecial = doctor_lis["doctor"][data]["specialization"]
                doctavail = doctor_lis["doctor"][data]["avail"]
                new_obj = {"f_name": doctfname, "l_name": doctlname, "id": doctid, "specialization": doctspecial,
                           "avail": doctavail}
            if count is 0:
                return None
            else:
                return new_obj
    except SystemError:
        print("Name Error")


def search_pat_name(patient_name):
    count = 0
    try:
        patient_lis = json.load("Patient.json", "r")
        name_keys = list(patient_lis["patient"].keys())
        for data in name_keys:
            if patient_lis["patient"][data]["f_name"] == patient_name or patient_lis["patient"][data]["id"] == patient_name or patient_lis["patient"][data]["mob_number"] == patient_name:
                count += 1
                patid = patient_lis["patient"][data]["id"]
                patfname = patient_lis["patient"][data]["f_name"]
                patlname = patient_lis["patient"][data]["l_name"]
                patmob = patient_lis["patient"][data]["mob_num"]
                new_obj = {"id": patid, "f_name": patfname, "l_name":patlname, "mob_num": patmob}
            if count is 0:
                return None
            else:
                return new_obj
    except SystemError:
        print("Name Error")


def display_doct():
    print("The Doctor Details are:")

    doc_json = json.load(open("Doctor.json", "r"))
    name_keys = list(doc_json["doctor"].keys())
    print('\t ID\t First Name\t Last Name\t Specialization \t Availability')
    for data in name_keys:
        print(doc_json["doctor"][data]["id"], '\t', doc_json["doctor"][data]["f_name"], '\t', doc_json["doctor"][data]["l_name"], '\t', doc_json["doctor"][data]["specialization"], '\t', doc_json["doctor"][data]["avail"])


def display_pat():
    print("The Patient Details are:")

    pat_json = json.load((open("Patient.json", "r")))
    name_keys = list(pat_json["patient"].keys())
    print('\t ID \t First Name\t Last Name \t Mobile')
    for data in name_keys:
        print(pat_json["patient"][data]["id"], '\t', pat_json["patient"][data]["f_name"], '\t', pat_json["patient"][data]["l_name"], '\t', pat_json["patient"][data]["mob_num"])
        print('\n')


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
