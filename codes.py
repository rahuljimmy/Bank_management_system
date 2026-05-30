import json
import random
import string
from pathlib import Path


class Bank:

    database = "data.json"

    @classmethod
    def load_data(cls):

        if Path(cls.database).exists():

            with open(cls.database, "r") as fs:
                return json.load(fs)

        return []

    @classmethod
    def save_data(cls, data):

        with open(cls.database, "w") as fs:
            json.dump(data, fs, indent=4)

    @classmethod
    def generate_account_number(cls):

        chars = (
            random.choices(string.ascii_uppercase, k=3)
            + random.choices(string.digits, k=4)
        )

        random.shuffle(chars)

        return "".join(chars)

    @classmethod
    def create_account(cls, name, age, email, pin):

        data = cls.load_data()

        # validations

        if not name or not email or not pin:
            return False, "Please fill all fields"

        if age < 18:
            return False, "Age must be 18+"

        if not str(pin).isdigit():
            return False, "PIN must contain numbers only"

        if len(str(pin)) != 4:
            return False, "PIN must be exactly 4 digits"

        if str(pin) in ["1234", "0000", "1111"]:
            return False, "Weak PIN. Choose a stronger PIN"

        # check duplicate email

        for user in data:

            if user.get("email") == email:
                return False, "Email already registered"

        acc_no = cls.generate_account_number()

        user = {
            "name": name,
            "age": age,
            "email": email,
            "pin": int(pin),
            "account_no": acc_no,
            "balance": 0,
        }

        data.append(user)

        cls.save_data(data)

        return True, user

    @classmethod
    def find_user(cls, acc_no, pin):

        data = cls.load_data()

        if not acc_no or not pin:
            return False, "Please fill all fields"

        for user in data:

            if user.get("account_no") == acc_no:

                if user.get("pin") != pin:
                    return False, "Invalid PIN"

                return True, user

        return False, "Account not found"

    @classmethod
    def deposit(cls, acc_no, pin, amount):

        data = cls.load_data()

        if not acc_no or not pin:
            return False, "Please fill all fields"

        for user in data:

            if user.get("account_no") == acc_no:

                if user.get("pin") != pin:
                    return False, "Invalid PIN"

                if amount <= 0:
                    return False, "Amount must be greater than 0"

                if amount > 100000:
                    return False, "Deposit limit is 100000"

                user["balance"] += amount

                cls.save_data(data)

                return True, f"₹{amount} deposited successfully"

        return False, "Account not found"

    @classmethod
    def withdraw(cls, acc_no, pin, amount):

        data = cls.load_data()

        if not acc_no or not pin:
            return False, "Please fill all fields"

        for user in data:

            if user.get("account_no") == acc_no:

                if user.get("pin") != pin:
                    return False, "Invalid PIN"

                if amount <= 0:
                    return False, "Amount must be greater than 0"

                if user["balance"] == 0:
                    return False, "Your account balance is 0"

                if user["balance"] < amount:
                    return False, "Insufficient balance"

                if user["balance"] <= 50:
                    return False, "Low balance warning"

                user["balance"] -= amount

                cls.save_data(data)

                return True, f"₹{amount} withdrawn successfully"

        return False, "Account not found"

    @classmethod
    def update_user(cls, acc_no, pin, name=None, email=None, new_pin=None):

        data = cls.load_data()

        if not acc_no or not pin:
            return False, "Please fill all fields"

        for user in data:

            if user.get("account_no") == acc_no:

                if user.get("pin") != pin:
                    return False, "Invalid PIN"

                if name:
                    user["name"] = name

                if email:
                    user["email"] = email

                if new_pin:

                    if not str(new_pin).isdigit():
                        return False, "PIN must contain numbers only"

                    if len(str(new_pin)) != 4:
                        return False, "PIN must be exactly 4 digits"

                    user["pin"] = int(new_pin)

                cls.save_data(data)

                return True, "User details updated successfully"

        return False, "Account not found"

    @classmethod
    def delete_user(cls, acc_no, pin):

        data = cls.load_data()

        if not acc_no or not pin:
            return False, "Please fill all fields"

        for i, user in enumerate(data):

            if user.get("account_no") == acc_no:

                if user.get("pin") != pin:
                    return False, "Invalid PIN"

                data.pop(i)

                cls.save_data(data)

                return True, "Account deleted successfully"

        return False, "Account not found"