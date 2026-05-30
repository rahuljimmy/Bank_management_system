# 🏦 Bank Management System (Python Project)

A professional and interactive **Bank Management System** built using **Python** and Streamlit.  
This project simulates real-world banking operations through a clean, user-friendly, and interactive web application.

The application allows users to:

✔ Create Bank Accounts  
✔ Deposit Money  
✔ Withdraw Money  
✔ View Account Details  
✔ Update User Information  
✔ Delete Bank Accounts  

---

# 🚀 Project Highlights

✔ Interactive Streamlit Web Application  
✔ Secure PIN-Based Authentication  
✔ JSON-Based Data Storage  
✔ Deposit & Withdrawal Management  
✔ Real-Time Success & Error Notifications  
✔ Strong Input Validation System  
✔ Beginner-Friendly Banking Project  
✔ Clean & Interactive UI
✔ Successfully Deployed on Streamlit Cloud

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend Logic |
| Streamlit | Web Application |
| JSON | Database Storage |
| VS Code | Development Environment |

---

# ✨ Key Features

## 🔐 Create Account

- Create new bank accounts securely
- Auto-generated unique account numbers
- Age validation (18+ only)
- Strong 4-digit PIN validation
- Duplicate email prevention

---

## 💰 Deposit Money

- Deposit money into existing accounts
- Secure PIN verification
- Deposit limit validation
- Instant balance updates

---

## 💸 Withdraw Money

- Secure withdrawal system
- Insufficient balance detection
- Low balance warnings
- PIN authentication

---

## 📄 Show Account Details

Users can securely view:

- Name
- Age
- Email
- Account Number
- Account Balance

Using:
- Account Number
- PIN

---

## 🛠️ Update User Information

Users can update:

✔ Name  
✔ Email  
✔ PIN  

---

## ❌ Delete Account

- Permanently remove bank accounts
- Secure authentication required

---

# 🧠 Input Validations

This project includes multiple real-world validations such as:

✅ Age must be 18+  
✅ PIN must contain exactly 4 digits  
✅ Weak PIN detection  
✅ Invalid PIN handling  
✅ Empty field checking  
✅ Account existence verification  
✅ Deposit limit checking  
✅ Insufficient balance handling  

---

# 🎨 Interactive User Experience

The application provides:

🟢 Green Success Notifications  
🔴 Red Error Notifications  
🟡 Warning Messages  

Using Streamlit alert components like:

```python
st.success()
st.error()
st.warning()
