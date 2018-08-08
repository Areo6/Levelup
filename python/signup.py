import re
import os

class Signup(object):
    """Object representation of the Uber signup page"""

    def __init__(self):
        self.f_name = ""
        self.s_name = ""
        self.phone_num = 0
        self.e_mail = ""
        self.pass_word = ""
        self.done = False
        file = self.create_user_file()
    
    def menu(self):
        #Displays the menu for the menu for Uber signup page
        for i in range(5):
            j = 0    
            print("                           ",end = ' ')
            if i == 0 or i == 4:
                while j < 6:
                    if j == 5:
                        print("*")
                    else:
                        print("*", end = ' ')
                    j += 1
            elif i == 2:
                while j < 6:
                    if j == 0:
                        print("*", end = ' ')
                    elif j == 1:
                            print("U",end = ' ')
                    elif j == 2:
                            print("b",end = ' ')
                    elif j == 3:
                        print("e",end = ' ')
                    elif j == 4:
                        print("r",end = ' ')
                    else:
                        print("*")
                    j += 1
            else:
                while j < 6:
                    if j == 0:
                            print("*", end = ' ')
                    elif j == 5:
                        print("*")
                    else:
                        print(" ", end = ' ')
                    j += 1
        header = """                         Sign up to ride
                Safe, reliable trips in minutes"""
        print(header)
        prompt = """  

            (A)dd User
            (S)ee users
            (Q)uit
            
        Enter Your choice:""" 

        while not self.done:
            chosen = False
            while not chosen:
                try:
                    choice = input(prompt).strip()[0].lower()
                except (KeyboardInterrupt, EOFError):
                    choice = 'q'
                if choice not in("asq"):
                    print("Wrong choice...Please chose again.")
                else:
                    chosen = True
            if choice == "a": self.firstname()
            if choice == "s": self.display_users()
            if choice == "q": self.done = True
        
    def firstname(self):
        # To input first name
        valid = False
        while not valid:
            self.f_name = input("First Name :  ").strip()
            if self.f_name == "":
                print("Fist name can't be empty, Try again.")
            else:
                valid = True
        self.surname()

    def surname(self):
        # To input Surname
        valid = False
        while not valid:
            self.s_name = input("Surname :  ").strip()
            if self.s_name == "":
                print("Surnamecan't be empty. Please try again.")
            else:
                valid = True
        self.phone()
        
    def phone(self):
        finish = False
        while not finish:
            try:
                self.phone_num = int(input("Phone Number :  ").strip())
            except (Exception):
                print("Numbers only allowed. Try again.")
                continue
            phone_str = str(self.phone_num)
            if phone_str[0] != "0":
                print("Phone number should biggin with 0. Try again")
                continue
            if len(phone_str) != 10:
                print("Phone number should be 10 diggits.")
                continue
            try:
                int(self.phone_num)
                finish = True
            except Exception:
                print("Only numeric values allowed")
        self.email()

    def email(self):
        finish = False
        while not finish:
            self.e_mail = input("Email :  ").strip()
            is_valid = re.search(r"[\w-]+@[\w.-]+\.+", self.e_mail)
            if is_valid:
                finish = True
                self.password()
            else:
                print("Wrong email. Please try again")

    def password(self):
        self.pass_word = input("Password :  ").strip()
        popup = input("Save? y/n : ").strip()[0].lower()
        if popup ==  "y":
            self.save()
        else:
            pass
    
    @staticmethod
    def create_user_file():
        if not os.path.exists("signup.txt"):
            f = open("signup.txt",'w')
            f.write("UBER's USER DETAILS".center(100))
            f.close()
        
    def save(self):
        f = open("signup.txt",'a')
        f.write("\n" + "---------------------".center(100))
        f.write("\n\n" + "First Name = " + self.f_name)
        f.write("\n" + "Surname = " + self.s_name)
        f.write("\n" + "Phone Number = " + self.phone_num)
        f.write("\n" + "Email = " + self.e_mail)
        f.write("\n" + "Password = " + self.pass_word)
        f.close()

    def display_users(self):
        try:
            f = open("signup.txt",'r')
        except (IOError, e):
            print("Sorry, couldn't open file.")
        else:
            for line in f:
                print(line, end = " ")
            
        f.close()

if __name__ == "__main__":
    signup = Signup()
    signup.menu()