import unittest
from user import User


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_init(self):
        self.assertIsInstance(self.user.firstname, str)
        self.assertIsInstance(self.user.surname, str)
        self.assertIsInstance(self.user.phone, int)
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
    
    def test_add_fistname_if_returns_type_string(self):
        firstname = "Malaba"
        self.assertRaises(TypeError ,self.user.add_firstname(firstname), "Type error raised")
    
    def test_add_surname_if_returns_type_string(self):
        
        surname = []
        with self.assertRaises(TypeError):
             self.user.surname(surname)



if __name__ == "__main__":
    unittest.main()