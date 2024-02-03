import re
import logging

logging.basicConfig(filename='registration.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, format='%(asctime)s:%(filename)s:%(lineno)s:%(levelname)s:%(message)s')

class UserRegistration:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._username = None
        self._email = None
        self._mobile_number = None
        self._password = None

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value
    
    @property
    def mobile_number(self):
        return self._mobile_number

    @mobile_number.setter
    def mobile_number(self, value):
        self._mobile_number = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    def username_validation(self, first_name, last_name):
        try:
            pattern_username = "^[A-Z][a-z]{3}"
            result = re.match(pattern_username, first_name)
            result2 = re.match(pattern_username, last_name)
            
            if result and result2:
                self.username = f"{first_name} {last_name}"
                print(f"Hello {self.username}, How are you?")
            else:
                raise ValueError("Invalid username, enter proper username") 
        except ValueError as e:
            self.username = e
            self.logger.error(e)

    def email_validation(self, enter_email):
        try:
            email_pattern = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
            check_email = re.search(email_pattern, enter_email)
            if check_email:
                self.email = enter_email
            else:
                raise ValueError("Invalid email, enter proper email id")
        except ValueError as e:
            self.email = e
            self.logger.error(e)

    def mobile_valid(self, mobile_enter):
        try:
            mobile_pattern = "^[0-9]{2,2} [0-9]{10}"
            check_mobile = re.search(mobile_pattern, mobile_enter)
            if check_mobile:
                self.mobile_number = mobile_enter
            else:
                raise ValueError("Invalid mobile, enter again")
        except ValueError as e:
            self.mobile_number = e
            self.logger.error(e)

    def password_validation(self, pass_enter):
        try:
            password_pattern = (
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"
            )
            check_pass = re.search(password_pattern, pass_enter)
            if check_pass:
                self.password = pass_enter
            else:
                raise ValueError("Invalid password, enter again")
        except ValueError as e:
            self.password = e
            self.logger.error(e)

if __name__ == "__main__":
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    enter_email = input("Enter your email: ")
    mobile_enter = input("Enter your mobile number: ")
    pass_enter = input("Enter your password: ")

    user_reg = UserRegistration()
    user_reg.username_validation(first_name, last_name)
    user_reg.email_validation(enter_email)
    user_reg.mobile_valid(mobile_enter)
    user_reg.password_validation(pass_enter)


