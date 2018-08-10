import unittest
from user import User


class UserTest(unittest.TestCase):

    def setUp(self):
        self.user = User()
    
    def test_set_firstname_raise_exception_if_type_is_not_str(self):
        firstname = "Malaba"
        self.assertRaises(TypeError ,self.user.set_firstname(firstname))

    def test_set_firstname_returns_msg_if_firtname_not_string_or_empty_str(self):
        firstname = ""
        self.assertEqual(self.user.set_firstname(firstname), "First name can't be Empty")

    def test_set_firstname_if_firstname_is_valid(self):
        firstname = "Sudi"
        self.assertIsNone(self.user.set_firstname(firstname),"Invalid name")
    
    def test_set_surname_raise_exception_if_type_is_not_str(self):
        surname = "Malaba"
        self.assertRaises(TypeError ,self.user.set_surname(surname))

    def test_set_surname_returns_msg_if_suname_not_string_or_empty_str(self):
        surname = ""
        self.assertEqual(self.user.set_surname(surname), "Surname can't be Empty")

    def test_set_surname_if_name_is_valid(self):
        surname = "Sudi"
        self.assertIsNone(self.user.set_surname(surname),"Invalid name")
    # def test_add_surname_if_returns_type_string(self):
    #     surname = []
    #     with self.assertRaises(TypeError):
    #          self.user.surname(surname)

    # def test_add_phone_number_argument_is_integer(self):
    #     phone = 1
    #     self.assertRaises(TypeError, self.user.add_phone_number(phone))

    # def test_add_email_is_in_valid_string_format(self):
    #     email = "eubule@gmail.com"
    #     with self.assertRaises(TypeError):
    #          self.user.email(email)
    #     self.assertIn("@", email)
    #     self.assertIn(".", email)

    # def test_password_is_not_null(self):
    #     password = "Eric"
    #     self.assertNotEqual(self.user.add_password(password), "")


if __name__ == "__main__":
    unittest.main()