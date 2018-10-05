import re

try:
    def namevalidate(name):
        if re.search("^[A-Za-z]{2,20}", name):
            return True
        else:
            return False


    def fnamevalidate(fname):
        if re.search("[\wA-Za-z]{2,20}\s\w[A-Za-z]{2,20}", fname):
            return True
        else:
            return False


    def mobilevalidate(mobile):
        if re.search("\w{10}", mobile):
            return True
        else:
            return False


    def datevalidate(date):
        if re.search("^[\d]{2}/[\d]{2}/[\d]{4}", date):
            return True
        else:
            return False

    expression = '''
    Hello <<name>>, 
    We have your full name as <<full name>> in our system. 
    Your contact number is 91-xxxxxxxxxx.
    Please,let us know in case of any clarification.
    Thank you 
    BridgeLabz 
    01/01/2016.
    '''

    name = input('Enter your name')
    fname = input("Enter your full name")
    mobile = input("Enter your mobile number")
    date = input("Enter the date")

    nameval = namevalidate(name)

    fnameval = fnamevalidate(fname)

    mobileval = mobilevalidate(mobile)

    dateval = datevalidate(date)

    if nameval and fnameval and mobileval and dateval:
        expression = re.sub("<<name>>", name, expression)
        expression = re.sub("<<full name>>", fname, expression)
        expression = re.sub("91-xxxxxxxxxx", mobile, expression)
        expression = re.sub("01/01/2016", date, expression)
        print(expression)
    else:
        print("Invalid Expression")
        exit(0)

except Exception:
    print("Invalid Input Detected")