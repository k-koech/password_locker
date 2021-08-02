from user import Details, User
from cryptography.x509 import name


def create_user(username, password):
    """
    create_user creates a new_user 
    """
    new_user = User(username, password)
    return new_user


def sign_in(username, password):
    user_exists = User.user_exist(username, password)
    if sign_in != False:
        return user_exists

def save_user(user):
    user.save_user()

def create_details(username, password):
    new_details = Details(username, password)
    return new_details

def save_details(details):
    details.save_details()

def display_detail_list():
    return Details.display_details()

def delete_details(details):
    details.delete_details()

def main():
    print('Hi.Welcome to Password Locker.')
    print('\n')
    print('Select the short_cord to navigate through:')
    print('\n')
    print('to create new user use "NU":')
    print('\n')
    print('to login use "LG" or "Ex" to exit')
    print('\n')
    print('to delete Account use "DU"')
    short_code = input().lower()
    if short_code == 'nu':
        print('Enter new account details')
        print('\n')
        username = input('Enter Username: ')
        while True:
            print('CP = to create password')
            password_choice = input().lower()
            if password_choice == 'cp':
                password = input('Confirm Password: ')
                print('\n')

            else:
                print('Invalid password. Try again')
            save_user(create_user(username, password))

        print('\n')
        print(
            f'Welcome {username} to your account')
        print('\n')

    elif short_code == 'lg':
        print('Enter Your Account Username and Password to Login')
        username = input('Username:')
        password = input('Password:')
        check_user = sign_in(username, password)
        if sign_in == check_user:
            print(f'Welcome back {username}')
            print('\n')

        elif short_code == 'du':
            print('Are you sure want to delete Account??? If YES,type')
            username = input('Username :')
            password = input('Password:')
            check_user = sign_in(username, password)
            if sign_in == check_user:
                print(f'Account {username} has been successfully deleted ')
                print('\n')

            else:
                print('Incorrect account name')
                print('\n')


        elif short_code == 'ex':
            print('We are Sorry to see you leave!!!!')
            print('\n')

        else:
            print('Invalid Pasword. Try again!')
            print('\n')


if __name__ == '__main__':
    main()