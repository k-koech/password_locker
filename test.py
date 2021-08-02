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

    def tearDown(self):

        Details.detail_list = []

    def test_save_multiple_accounts(self):

        self.new_details.save_details()
        test_details = Details('LinkedIn', 'Collo', 'Koech')
        test_details.save_details()
        self.assertEqual(len(Details.detail_list),2)

    def test_delete_details(self):

        self.new_details.save_details()
        test_details = Details('FB', 'Collo', 'Koech1')
        test_details.save_details()
        self.new_details.delete_details()
        self.assertEqual(len(Details.detail_list),1)

    def test_find_details(self):

        self.new_credentials.save_details()
        test_details = Details('Twitter', 'Dorothy', 'Muhonja5')
        test_details.save_details()
        find_details = Details.find_account_name('Twitter')
        self.assertEqual(find_details.account_name,test_details.account_name)
    
    def test_details_exist(self):
        """
        test to check if we can return True or False in regards to finding the details
        """
        self.new_details.save_details()
        test_details = Details('Twitter','Dorothy','Muhonja5')
        test_details.save_details()
        details_exist = Details.details_exist('Twitter')
        self.assertTrue(details_exist)

    def display_details(self):
        """
        Displays all details saved by the user
        """
        self.assertEqual(Details.display_details(), Details.credential_list)
    
    def test_generate_password(self):
        generated_password = self.new_details.generate_password()
        self.assertEqual(len(generated_password), 8)


if __name__ == '__main__':
    unittest.main()
