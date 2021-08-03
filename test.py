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

    
 
if __name__ == '__main__':
    unittest.main()