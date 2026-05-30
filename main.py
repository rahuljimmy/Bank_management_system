import json
import random
import string
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occured as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k= 3)
        spchar = random.choices("!@#$%^&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)
    
    def CreateAccount(self):
        info = {"name" : input("Tell your name :- "),
                "age" : int(input("Tell your age :- ")),
                "email" : input("Tell your email :- "),
                "pin" : int(input("Tell your 4 digit pin :- ")),
                "accountNo" : Bank.__accountgenerate(),
                "balance" : 0}
        if info['age'] < 18 or len(str(info['pin'])) != 4:
            print("Sorry, you cannot create your account")
        else:
            print("Account has been created succesfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("Please note down your account number")
            Bank.data.append(info)
            Bank.__update()
    
    def DepositMoney(self):
        accnumber = input("please tell your account number :- ")
        pin = int(input("please tell your pin as well :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry, no data found")
        
        else:
            amount = int(input("how much money you want to depoit :- "))
            if amount  > 10000 or amount < 0:
                print("Sorry the amount is too much, you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully")
    

    def WithdrawMoney(self):
        accnumber = input("please tell your account number :- ")
        pin = int(input("please tell your pin as well :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry, no data found")
        
        else:
            amount = int(input("how much money you want to withdraw :- "))
            if userdata[0]['balance']  < amount:
                print("Sorry, you dont have that much money")
              
            else:
                userdata[0]['balance'] -= amount
                Bank.__update()
                print("Amount withdrew successfully")


    def ShowDetails(self):

        accnumber = input("please tell your account number :- ")
        pin = int(input("please tell your pin aswell :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]
        print("your information are \n\n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")



    def UpdateDetails(self):
        accnumber = input("please tell your account number :- ")
        pin = int(input("please tell your pin aswell :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("no such user found")
        
        else:
            print("you cannot change the age, account number, balance")

            print("Fill the details for change or leave it empty if no change")

            newdata = {
                "name": input("please tell new name or press enter :- "),
                "email":input("please tell your new Email or press enter to skip :- "),
                "pin": input("enter new Pin or press enter to skip :- ")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']
            
            newdata['age'] = userdata[0]['age']
            newdata['accountNo'] = userdata[0]['accountNo']
            newdata['balance'] = userdata[0]['balance']
            
            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])
            

            for i in newdata:
                 if newdata[i] == userdata[0][i]:
                     continue
                 else:
                     userdata[0][i] = newdata[i]

            Bank.__update()
            print("details updated successfully")


    def DeleteAccount(self):
        accnumber = input("please tell your account number :- ")
        pin = int(input("please tell your pin as well :- "))

        userdata = [i for i in Bank.data if i['accountNo'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("Sorry, no such data exist")
        else:
            check = input("press y if you actually want to delete the account or press n :- ")
            if check == 'n' or check == "N":
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()    

    
user = Bank()

print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("tell you responce :- "))

if check == 1:
    user.CreateAccount()

if check == 2:
    user.DepositMoney()

if check == 3:
    user.WithdrawMoney()

if check == 4:
    user.ShowDetails()

if check == 5:
    user.UpdateDetails()

if check == 6:
    user.DeleteAccount()
