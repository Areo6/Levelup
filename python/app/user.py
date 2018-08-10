import re

class User():
    """This class creates new user with a first name, surname, phone number, email and password"""

    def __init__(self, firstname = "", surname = "", phone = 0, email = "", password = ""):
        #Initializes fields to add a new user with their data type.
        self.firstname = str(firstname)
        self.surname = str(surname)
        self.phone = int(phone)
        self.email = str(email)
        self.password = str(password)

    def set_firstname(self, firstname):
        """This method is meant to add the first name to the user"""
        if not isinstance(firstname, str):
            raise TypeError("First name should be a string")
        if firstname.strip() == "":
            return "First name can't be Empty"
        self.firstname = firstname

    def set_surname(self,surname):
        """This method takes in a surname and adds it to the user for a valid string"""
        if not isinstance(surname, str):
            raise TypeError("Surname should be a string")
        if surname.strip() == "":
            return "Surname can't be Empty"
        self.surname = surname

    def set_phone_number(self, phone):
        """This class takes in a phone number and validates it."""
        if not isinstance(phone, int):
            raise TypeError("Phone Number should be an Integer Number")
        phone_str = str(phone)
        if len(phone_str) < 6:
            return "Invalid number. Should biggin with 0 with at least 6 digits"
        self.phone = phone

    def set_email(self, email):
        """This method takes in a email input, checks if valid the add it"""
        if not isinstance(email, str):
            raise TypeError("Email should be a string")
        is_valid = re.search(r"[\w-]+@[\w-]+\.+", email)
        if not is_valid:
            return "Invalid email."
        self.email = email

    def set_password(self, password):
        """Takes a password as log as it's ot null"""
        if not isinstance(password, str):
            raise TypeError("Password should be a string")
        if password.strip() == "":
            return "Password can't be Empty"
        self.password = password

    def get_firstname(self):
        #Returns the First name
        self.set_firstname(self.firstname)
        return self.firstname

    def get_surname(self):
        #Returns surname and raises Type Error if input not a string.
        self.set_surname(self.surname)
        return self.surname

    def get_phone_number(self):
        #This method returns a phone number for the user
        self.set_phone_number(self.phone)
        return self.phone

    def get_email(self):
        #returns email for user if in right format
        self.set_email(self.email)
        return self.email

    def get_password(self):
        #Returns password add checks if password is not null
        self.set_password(self.password)
        return self.password

    def view_user(self):
        #This methods displays the details of the user
        print("Fist name: "+self.get_firstname())
        print("Surname: "+self.get_surname())
        print("Phone: {}".format(self.get_phone_number()))
        print("email: "+self.get_email())
        print("password: "+self.get_password())


if __name__ == "__main__":
    user = User()
    user.set_firstname("Malaba")
    user.set_surname("Mashauri")
    user.set_phone_number(7512)
    user.set_email("eubule@gmail.com")
    user.set_password("my_pass")
    user.view_user() 
    
