class Credentials:
    # Class that generates new instances of credentials.
   
    def __init__(self,account,password):

        self.account = account
        self.password = password
       
    credentials_list = [] # Empty credentials list
   
    def save_credential(self):
        # save_user method saves contact objects into user_list
        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        return cls.credentials_list

    def delete_contact(self):
        Credentials.credentials_list.remove(self)