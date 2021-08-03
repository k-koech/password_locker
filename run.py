#!/usr/bin/env python3.6
from os import system
import random
import string
from user import User
from credentials import Credentials

def create_user(username,password):
    '''
    Function to create a new contact
    '''
    new_user = User(username, password)
    return new_user

def save_users(user):
    ''' Function to save User # Init method up here    '''
    user.save_user()

def check_existing_users(username, password):
    '''
    Function that check if a contact exists with that username and password and return a Boolean
    '''
    return User.user_exist(username, password)

def find_user(username, password):
    '''
    Function that finds a contact by number and returns the contact
    '''
    return User.login(username, password)

#............... Accounts credentials..........................
def create_credentials(account,password):
    new_credentials = Credentials(account, password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credential()

def display_credentials():
    return Credentials.display_credentials()

def del_credentials(credentials):
    credentials.delete_credentials()





# ===================================================================
def main():
    print("Welcome to Password Locker.")
    print("Use the number codes")
    print("1. Create a new Account\n2. Login")
    account_code = input()

    if account_code == "1":
        print("Create your account")
        print("Username : ")    
        user_name = input()
        print("Password : ")
        password = input() 

        save_users(create_user(user_name,password)) # create and save new user.
        print('\n')
        print(f"New account {user_name} created")
        system('clear')

        # login after registration
        login()

    elif account_code == '2':
        login()

# RE-USABLE FUNCTIONS
# login function to be reused
def login():
    print("LOGIN")
    print("Username : ") 
    search_username = input()
    print("Passsword : ") 
    search_password = input()
    
    if check_existing_users(search_username, search_password):
            search_user = find_user(search_username, search_password)
            system('clear')
            print(f"Logged in as {search_user.username}")
            print('-' * 20)

            print("Choose the service you need")
            print("1. Store already existing account credentials ") 
            print("2. Create a new account credentials ")
            print("3. Display my credentials ")
            service_choice = input()

            if service_choice=="1":
                print("Store already existing account credentials")
                print("Enter your Account name")
                account_name = input()
                print("Enter your Account password")
                account_password = input()

                save_credentials(create_credentials(account_name, account_password)) # create and save new account credentials.
                print('\n')
                print(f"Credentials for {account_name} created successfully")
                system('clear')
                credentials()


            elif service_choice=="2":
                print("Create a NEW account credentials")
                print("Enter your Account name")
                account_name = input()

                print("Do you want a system generated password?")
                print("1. Yes\n2. No")
                choice = input()

                if choice=="1":
                    letters = string.ascii_letters
                    password = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
                    save_credentials(create_credentials(account_name, password)) # create and save new account credentials.
                    print('\n')
                    print(f"Credentials for {account_name} created successfully")
                    system('clear')
                    credentials()
                

                elif choice=="2":
                    print("Enter {account_name} 's Account password")
                    account_password = input()
                    save_credentials(create_credentials(account_name, account_password)) # create and save new account credentials.
                    print('\n')
                    print(f"Credentials for {account_name} created successfully")
                    system('clear')
                    credentials()

                    print("I really didn't get that. Please use numbers representing a choce")

                    print("Passsword : ") 
                    search_password = input()
                else:
                    print("Wrong choice! Try again")

            elif service_choice=="3":
                credentials()
            
            else:
                print("Invalid choice! Try again")

    else:
            system('clear')
            print("Wrong credentials or User does not exist !!")
            main()


def credentials():
    if display_credentials():
            print("Your credentials")
            for credentials in display_credentials():
                    print(f"Account                Password")
                    print(f"{credentials.account} {credentials.password}")
            print('\n')
    else:
            print('\n')
            print("You dont seem to have any contacts saved yet")
            print('\n')


def del_credentials():
    if display_credentials():
            print("Choose aacount to delete")
            for x in range(len(display_credentials)), credentials in display_credentials():
                    print(f"{x+1} {credentials.account}")
            del_credentials()
    else:
            print('\n')
            print("You dont seem to have any contacts saved yet")
            print('\n')

    # while True:
    #         print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")

    #         short_code = input().lower()

    #         if short_code == 'cc':
    #                
    #                 save_users(create_user(f_name,l_name,p_number,e_address)) # create and save new contact.
    #                 print ('\n')
    #                 print(f"New Contact {f_name} {l_name} created")
    #                 print ('\n')

    #         elif short_code == 'dc':

    #                 if display_contacts():
    #                         print("Here is a list of all your contacts")
    #                         print('\n')

    #                         for contact in display_contacts():
    #                                 print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

    #                         print('\n')
    #                 else:
    #                         print('\n')
    #                         print("You dont seem to have any contacts saved yet")
    #                         print('\n')

    #         elif short_code == 'fc':

    #                 print("Enter the number you want to search for")

    #                 search_number = input()
    #                 if check_existing_users(search_number):
    #                         search_contact = find_contact(search_number)
    #                         print(f"{search_contact.first_name} {search_contact.last_name}")
    #                         print('-' * 20)

    #                         print(f"Phone number.......{search_contact.phone_number}")
    #                         print(f"Email address.......{search_contact.email}")
    #                 else:
    #                         print("That contact does not exist")

    #         elif short_code == "ex":
    #                 print("Bye .......")
    #                 break
    #         else:
    #                 print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()