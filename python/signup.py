class Signup(object):
    """Object representation of the Uber signup page"""

    def __init__(self):
        self.f_name = ""
        self.s_name = ""
        self.phone_num = 0
        self.e_mail = ""
        self.pass_word = ""
    
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
            (F)ist Name
            s(U)rname
            (P)hone Number
            (E)mail
            p(A)ssword
            (S)ave
            
        Enter Your choice:"""
        done = False 
        while not done:
            chosen = False
            while not chosen:
                try:
                    choice = input(prompt).strip()[0].lower()
                except (KeyboardInterrupt, EOFError):
                    choice = 'q'
                if choice not in("fupeas"):
                    print("Wrong choice...Please chose again.")
                else:
                    chosen = True
            if choice == "f": self.firstname()
            if choice == "u": self.surname()
            if choice == "p": self.phone()
            if choice == "e": self.email()
            if choice == "a": self.password()
            if choice == "s": 
                f = open("signup.txt",'w')
                f.write("UBER's USER DETAILS".center(100))
                f.write("\n" + "---------------------".center(100))
                f.write("\n\n\n" + "First Name = " + self.f_name)
                f.write("\n" + "Surname = " + self.s_name)
                f.write("\n" + "Phone Number = " + self.phone_num)
                f.write("\n" + "Email = " + self.e_mail)
                f.write("\n" + "Password = " + self.pass_word)
                f.close()
                done = True
        
    def firstname(self):
        self.f_name = input("First Name:  ").strip()

    def surname(self):
        self.s_name = input("Surname:  ").strip()
        
    def phone(self):
        done = False
        while not done:
            self.phone_num = input("Phone Number:  ").strip()
            phone_str = str(self.phone_num)
            if phone_str[0] != "0":
                print(phone_str+"Phone number should biggin with 0. Try again")
                continue
            if len(phone_str) != 10:
                print("Phone number should be 10 diggits.")
                continue
            try:
                int(self.phone_num)
                done = True
            except Exception:
                print("Only numeric values allowed")

    def email(self):
        self.e_mail = input("Email:  ").strip()

    def password(self):
        self.pass_word = input("Password:  ").strip()

if __name__ == "__main__":
    signup = Signup()
    signup.menu()