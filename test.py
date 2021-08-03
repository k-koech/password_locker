import unittest # Importing the unittest module
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    def setUp(self):
        self.new_user = User("Triple_K","kkkk") 


    def test_init(self):
        self.assertEqual(self.new_user.username,"Triple_K")
        self.assertEqual(self.new_user.password,"kkkk")
    
    def test_save_user(self):
            self.new_user.save_user() # saving the new contact
            self.assertEqual(len(User.user_list),1)

      
    def tearDown(self):
            User.user_list = []

    def test_save_multiple_User(self):
            self.new_user.save_user()
            test_user = User("Triple_K","kip123") 
            test_user.save_user()
            self.assertEqual(len(User.user_list),2)
    
    def test_login(self):
        self.new_user.save_user()
        test_user = User("Triple_K","kip123") 
        test_user.save_user()

        auth_user = User.login("Triple_K","kip123")

        # self.assertEqual(auth_user.username,auth_user.password)


    # credentials tests
class TestCredentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("FaceBook","kip123") 


    def test_init(self):
        self.assertEqual(self.new_credentials.account,"FaceBook")
        self.assertEqual(self.new_credentials.password,"kip123")
    
    def test_save_credentials(self):
            self.new_credentials.save_credential()
            self.assertEqual(len(Credentials.credentials_list),2)

    def test_display_all_credentials(self):
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

    def test_delete_credentials(self):
            self.new_credentials.save_credential()
            test_credentials = Credentials("FaceBook","kip123") 
            test_credentials.save_credential()
            self.new_credentials.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)



  
 

 
if __name__ == '__main__':
    unittest.main()