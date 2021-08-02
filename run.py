from user import Details, User
from cryptography.x509 import name


def create_user(username, password):
    """
    create_user creates a new_user 
    """
    new_user = User(username, password)
    return new_user



if __name__ == '__main__':
    main()