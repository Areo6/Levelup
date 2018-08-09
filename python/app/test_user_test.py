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

    def test_add_phone_number_argument_is_integer(self):
        phone = 1
        self.assertRaises(TypeError, self.user.add_phone_number(phone))

    def test_add_email_is_in_valid_string_format(self):
        email = "eubule@gmail.com"
        with self.assertRaises(TypeError):
             self.user.email(email)
        self.assertIn("@", email)
        self.assertIn(".", email)

    def test_password_is_not_null(self):
        password = "Eric"
        self.assertNotEqual(self.user.add_password(password), "")


if __name__ == "__main__":
    unittest.main()