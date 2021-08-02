import unittest
from user import User, Details

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User('Collo', 'Collo2')

    def test_init(self):

        self.assertEqual(self.new_user.username,'Collo')
        self.assertEqual(self.new_user.password,'Collo2')

    def test_save_user(self):

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


class TestDetails(unittest.TestCase):

    def setUp(self):
        self.new_details = Details('Inst', 'Collo', 'Collo2')

    def test_init(self):

        self.assertEqual(self.new_details.account_name, 'Inst')
        self.assertEqual(self.new_details.username, 'Collo')
        self.assertEqual(self.new_details.password, 'Collo2')



if __name__ == '__main__':
    unittest.main()
