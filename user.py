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

    @classmethod
    def user_exist(cls,username,password):
        """
        user_exist confirms if the user exist in the user_list
        """

        current_user = ''
        for user in User.user_list:
            if(user.username == username and user.password == password):
                current_user = user.name
            return current_user

class Details:

    detail_list = []

    def __init__(self, username, password):

        self.username = username
        self.password = password

    def save_details(self):
        """
        save_details saves new details in the detail_list
        """
        Details.detail_list.append(self)

    def delete_details(self):
        """
        delete_details deletes a saved details in the detail_list
        """
        Details.detail_list.remove(self)  
