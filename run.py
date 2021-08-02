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


if __name__ == '__main__':
    main()