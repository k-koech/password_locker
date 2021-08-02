class User:
    """
    Create User class that generates new user instance
    """

    user_list = []

    def __init__(self,username,password):

        self.username = username
        self.password = password

    def save_user(self):
        """
        save_user method saves a new user objects to the user_list
        """
        User.user_list.append(self)

    