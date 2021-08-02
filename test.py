import unittest
from user import User, Details

class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User('Collo', 'Collo2')

    def test_init(self):

        self.assertEqual(self.new_user.username,'Collo')
        self.assertEqual(self.new_user.password,'Collo2')






if __name__ == '__main__':
    unittest.main()
