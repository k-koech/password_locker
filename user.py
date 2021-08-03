class User:
    # Class that generates new instances of users.
   
    def __init__(self,username,password):

        self.username = username
        self.password = password
       
    user_list = [] # Empty user list
   
    def save_user(self):
        # save_user method saves contact objects into user_list
        User.user_list.append(self)

    @classmethod
    def user_exist(cls,username,password):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for user in cls.user_list:
            if user.username == username and user.password==password:
                return True

        return False

    @classmethod
    def login(cls,username,password):
        '''
        Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
        '''
        for user in cls.user_list:
            if user.username == username and user.password==password:
                return user


# DONE


    def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        User.contact_list.remove(self)


    
    
    

  


