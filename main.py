"""Bank Management OOP Project"""
import json
import random
import string
from pathlib import Path


class Bank:

    database=Path(r'C:\Users\daksh\OneDrive\Desktop\OOPS_PROJECT_PYTHON\data.json')
    data=[]

    try:
        if database.exists() :
            with open(database,'r') as fs:
                data=json.loads(fs.read())

        else:
            print("no such file exists")

    except Exception as err:
        print(f"An exception occured as {err} ")


    def update():
        with open(Bank.database,'r') as fs:
                fs.write(json.dumps(Bank.data))
        



    def create_bank_account(self):
        info={
            "name":input("Enter your name :- "),
            "age":int(input("Enter your age :- ")),
            "email":input("Enter your Email id :- "),
            "pin":int(input("Enter your 4 no. pin :- ")),
            "account_no":1234,
            "balance":0
        }

        if info['age']<18 or len(str(info["pin"]))!=4 :
            print("Sorry you cannot create your account ")

        else:
            print("Account has been created successfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")


        Bank.data.append(info)
        Bank.update()

        




user=Bank()
print("Press 1 to create an account")
print("Press 2 to deposit Money in the account")
print("Press 3 to withdraw money")
print("Press 4 to get details")
print("Press 5 to update details")
print("Press 6 to delete your account")

check = int(input("Tell your Response :- "))

if check==1:
    user.create_bank_account()


