import pickle
import random


def create_acct():
    acct = {}
    a = True
    acct_no = random.randrange(100000,999999)
    acct_holder_name = str(input("Enter Name of Account Holder - "))
    while a:
        acct_type = str(input("Enter type of Account(C/S) - "))
        if acct_type.lower() != 'c' and acct_type.lower() != 's':
            print("UNDEFINED ACCOUNT TYPE")
        if acct_type.lower() == 'c' or acct_type.lower() == 's':
            a = False
    initial_amt = int(input("Enter Initial Amount - "))
    print(f"\n\nAccount Created Successfully\nAccount Number - {acct_no}\n")
    acct['acct_no'] = acct_no
    acct['acct_holder_name'] = acct_holder_name
    acct['acct_type'] = acct_type.upper()
    acct['initial_amt'] = initial_amt
    with open("acct.dat","ab") as f:
        pickle.dump(acct,f)

def display_all_accts():
    accts = {}
    file = open('acct.dat', 'rb')
    try:
        while True:
            accts = pickle.load(file)
            print(f"\n{accts}\n")
    except EOFError:
        file.close()

def display_acct_details():
    acct_no = int(input("Enter Account Number - "))
    acct = {}
    with open('acct.dat','rb') as f:
        try:
            while True:
                acct = pickle.load(f)
                if acct['acct_no'] == acct_no:
                    print(f"\nAccount Number = {acct['acct_no']}\nAccount Holder = {acct['acct_holder_name']}\nAccount Type = {acct['acct_type']}\nAmount = {acct['initial_amt']}\n\n")
        except EOFError:
            f.close()


def deposit_withdraw():
    acct_no = int(input("Enter Account Number - "))
    choice = int(input(f"1.Deposit\n2.Withdraw\n\nEnter Choice - "))
    acct = {}
    found = False
    if choice == 1:
        deposit = int(input("Enter Amount to be Deposited - "))
        with open('acct.dat', 'rb+') as f:
            try:
                while True:
                    location = f.tell()
                    acct = pickle.load(f)
                    if acct['acct_no'] == acct_no:
                        acct['initial_amt'] += deposit
                        f.seek(location)
                        pickle.dump(acct,f)

            except EOFError:
                f.close()

    if choice == 2:
        withdraw = int(input("Enter Amount to Withdraw - "))
        with open('acct.dat', 'rb+') as f:
            try:
                while True:
                    location = f.tell()
                    acct = pickle.load(f)
                    if acct['acct_no'] == acct_no:
                        acct['initial_amt'] -= withdraw
                        f.seek(location)
                        pickle.dump(acct,f)

            except EOFError:
                f.close()

def modify_acct():
    acct_no = int(input("Enter Account Number - "))
    acct = {}
    with open('acct.dat', 'rb+') as f:
        try:
            while True:
                location = f.tell()
                acct = pickle.load(f)
                if acct['acct_no'] == acct_no:
                    a = True
                    name = str(input("Enter Account Holder Name - "))
                    while a:
                        type = str(input("Enter type of Account(C/S) - "))
                        if type.lower() != 'c' and type.lower() != 's':
                            print("UNDEFINED ACCOUNT TYPE")
                        if type.lower() == 'c' or type.lower() == 's':
                            a = False
                    acct['acct_holder_name'] = name
                    acct['acct_type'] = type.upper()
                    f.seek(location)
                    pickle.dump(acct,f)
        except EOFError:
            f.close()

if __name__ == '__main__':
    print("""
========================================================
                BANK SERVICES SYSTEM
========================================================
    """)
    running = True
    while running:
        choice = int(input(f"Enter your Choice:\n1.Create Account\n2.Display All Accounts\n3.Display Your Account\n4.Deposit (or) Withdraw\n5.Modify Account\n6.Exit\n\nEnter your choice(1~6) - "))
        if choice == 1:
            create_acct()
        elif choice == 2:
            display_all_accts()
        elif choice == 3:
            display_acct_details()
        elif choice == 4:
            deposit_withdraw()
        elif choice == 5:
            modify_acct()
        elif choice == 6:
            running = False
        else:
            print("Wrong Choice")
