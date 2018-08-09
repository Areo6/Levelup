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
        firstname = self.firstname
        return self.firstname

    def add_surname(self,surname):
        #Adds surname and raises Type Error if input not a string.
        if not isinstance(surname, str):
            raise TypeError("Surname should be a string.")
        surname = self.surname
        return surname

    
