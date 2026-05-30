import streamlit as st
from codes import Bank

st.set_page_config(page_title="Bank Management System", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Action",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "Show Details",
        "Update Info",
        "Delete Account",
    ],
)

# CREATE ACCOUNT

if menu == "Create Account":

    st.subheader("Create New Account")

    name = st.text_input("Your Name")

    age = st.number_input("Your Age", min_value=0, step=1)

    email = st.text_input("Your Email")

    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):

        success, result = Bank.create_account(
            name,
            int(age),
            email,
            pin,
        )

        if success:

            st.success("Account created successfully")

            st.info(f"Your Account Number: {result['account_no']}")

        else:
            st.error(result)

# DEPOSIT

elif menu == "Deposit":

    st.subheader("Deposit Money")

    acc_no = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    amount = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):

        success, msg = Bank.deposit(
            acc_no,
            int(pin) if pin else "",
            int(amount),
        )

        if success:
            st.success(msg)

        else:
            st.error(msg)

# WITHDRAW

elif menu == "Withdraw":

    st.subheader("Withdraw Money")

    acc_no = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    amount = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):

        success, msg = Bank.withdraw(
            acc_no,
            int(pin) if pin else "",
            int(amount),
        )

        if success:
            st.success(msg)

        else:
            st.error(msg)

# SHOW DETAILS

elif menu == "Show Details":

    st.subheader("Account Details")

    acc_no = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    if st.button("Show"):

        success, result = Bank.find_user(
            acc_no,
            int(pin) if pin else "",
        )

        if success:

            st.success("Account found successfully")

            st.json(result)

        else:
            st.error(result)

# UPDATE INFO

elif menu == "Update Info":

    st.subheader("Update Your Info")

    acc_no = st.text_input("Account Number")

    pin = st.text_input("Current PIN", type="password")

    name = st.text_input("New Name (Optional)")

    email = st.text_input("New Email (Optional)")

    new_pin = st.text_input("New PIN (Optional)")

    if st.button("Update"):

        success, msg = Bank.update_user(
            acc_no,
            int(pin) if pin else "",
            name,
            email,
            new_pin,
        )

        if success:
            st.success(msg)

        else:
            st.error(msg)

# DELETE ACCOUNT

elif menu == "Delete Account":

    st.subheader("Delete Account")

    acc_no = st.text_input("Account Number")

    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):

        success, msg = Bank.delete_user(
            acc_no,
            int(pin) if pin else "",
        )

        if success:
            st.success(msg)

        else:
            st.error(msg)