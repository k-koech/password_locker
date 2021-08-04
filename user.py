class User:
    """
        Class that generates new instances of Users.
    """
   
    def __init__(self,username,password):

        self.username = username
        self.password = password
       
    user_list = [] # Empty user list
   
    def save_user(self):
        '''
        This method saves User objects into user_list
        '''
        User.user_list.append(self)

    @classmethod
    def user_exist(cls,username,password):
        '''
        Method that checks if a user exists from the users list.
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.username == username and user.password==password:
                return True

        return False


    @classmethod
    def login(cls,username,password):
        '''
        Method that logs in a user if it exists from the user list.
        '''
        for user in cls.user_list:
            if user.username == username and user.password==password:
                return user


    
    
    

  


