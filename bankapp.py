#import random to generate random numbers and string, os to delete session file when login out and sys for exiting the app
import random
import string
import os
import sys


#function holding several options
def details():
    print("""
Choose one of the following options(1, 2, 3)
1 Create new bank account
2 Check Account Details
3 Logout
        """)


#main function which takes user input, login user and also exits user
def staff_validation():
#this statement opens a session text
    with open("session.txt", "w") as session:
        name = input("Enter username: ")
        password = input("Enter password: ")
#this section checks to see if user input matches the details in staff txt file
        with open("staff.txt") as myfile:
            for row in myfile:
                myfile = row.split(",")
                username1 = str(myfile[0])
                password1 = str(myfile[1])
                username2 = str(myfile[4])
                password2 = str(myfile[5])
                if (name == username1 and password == password1) or (name == username2 or password == password2):
                    print("Login successful")
                    while True:
                        details()
                        choice = input("Choose one of the options: ")
                        if choice == "1":
                            account_creation()
                        elif choice == "2":
                            account_validation()
                        elif choice == "3":
                            print("Logging Out")
                            session.close()
                            os.remove("session.txt")
                            break
                else:
                    print("Login failed")


#this section creates a file customer.txt file, creates accounts by taking input from user and appending to the customer.txt file
def account_creation():
    with open("customer.txt", "w") as file:
        name = str(input("Account name: ")).lower()
        balance = input("Opening balance: ")
        acc_type = str(input("Account type: ")).lower()
        email = str(input("Account email: ")).lower()
        print("Your account number is")
        account = "".join(random.choice(string.digits) for i in range(10))
        print(account)

        file.write("Account name is: " + name + "\r\n")
        file.write("Opening balance: " + str(balance) + "\r\n")
        file.write("Account type: " + acc_type + "\r\n")
        file.write("Account email: " + email + "\r\n")
        file.write("Your account number is: " + "" + str(account) + "\r\n")


def account_validation():
    enter_acc = input("Enter account number: ")
    with open("customer.txt", "r") as customer:
        for detail in customer:
            print(detail, end="")


while True:
    opt = input("Select one of the two options: \nStaff login(login)\nClose app(Close)\nEnter option: ")
    if opt == "login":
        staff_validation()
    elif opt == "Close":
        sys.exit()
    else:
        print("Select Valid Option")


