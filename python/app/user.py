class User():
    """This class creates new user with a first name, surname, phone number, email and password"""

    def __init__(self, firstname = "", surname = "", phone = 0, email = "", password = ""):
        #Initializes fields to add a new user with their data type.
        self.firstname = str(firstname)
        self.surname = str(surname)
        self.phone = int(phone)
        self.email = str(email)
        self.password = str(password)

    def add_firstname(self, firstname):
        #Adds the First name
        if not isinstance(firstname, str):
            raise TypeError("First name should be a string.")
        self.firstname = firstname
        return self.firstname

    def add_surname(self,surname):
        #Adds surname and raises Type Error if input not a string.
        if not isinstance(surname, str):
            raise TypeError("Surname should be a string.")
        self.surname = surname
        return self.surname

    def add_phone_number(self, phone):
        #This method add a phone number for the user
        if not isinstance(phone, int):
            raise TypeError("Phone number should be a number.")
        self.phone = phone
        return self.phone

    def add_email(self, email):
        #Adds email for user if in right format
        if isinstance(email, str):
            raise TypeError("Email should be in string format.")
        is_valid = re.search(r"[\w-]+@[\w.-]+\.+", email)
        if is_valid:
            self.email = email
        else:
            print("Wrong email format.")
        return self.email

    def add_password(self, password):
        #Adds password add checks if password is not null
        if password == "":
            print("Password can't be null")
        else:
            password = str(password).strip()
            self.password = password
        return password
            
    
