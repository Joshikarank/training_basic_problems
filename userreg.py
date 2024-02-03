import re
import logging

logging.basicConfig(filename='registration.log', filemode='w', encoding='utf-8',
                    level=logging.INFO, format='%(asctime)s:%(filename)s:%(lineno)s:%(levelname)s:%(message)s')

class UserRegistration:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._first_name = None
        self._last_name = None
        self._email = None
        self._mobile_number = None
        self._password = None

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

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

    def First_name(self):
        try:
            pattern_username = "^[A-Z][a-z]{3}"
            result = re.match(pattern_username, self.first_name)
            
            if result:
                print(f"Hello {self.first_name}")
            else:
                raise ValueError("Invalid first name, enter proper first name") 
        except ValueError as e:
            self.logger.error(e)
    
    def Last_name(self):
        try:
            pattern_username = "^[A-Z][a-z]{3}"
            result2 = re.match(pattern_username, self.last_name)
            
            if result2:
                print(f"Hello {self.last_name}")
            else:
                raise ValueError("Invalid last name, enter proper last name") 
        except ValueError as e:
            self.logger.error(e)

    def email_validation(self):
        try:
            email_pattern = "^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
            check_email = re.search(email_pattern, self.email)
            if not check_email:
                raise ValueError("Invalid email, enter proper email id")
        except ValueError as e:
            self.logger.error(e)

    def mobile_valid(self):
        try:
            mobile_pattern = "^[0-9]{2,2} [0-9]{10}"
            check_mobile = re.search(mobile_pattern, self.mobile_number)
            if not check_mobile:
                raise ValueError("Invalid mobile, enter again")
        except ValueError as e:
            self.logger.error(e)

    def password_validation(self):
        try:
            password_pattern = (
                "^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d)(?=.*[@$!%*?&])[A-Za-z\\d@$!%*?&]{8,}$"
            )
            check_pass = re.search(password_pattern, self.password)
            if not check_pass:
                raise ValueError("Invalid password, enter again")
        except ValueError as e:
            self.logger.error(e)

if __name__ == "__main__":
    user_reg = UserRegistration()

    user_reg.first_name = input("Enter your first name: ")
    user_reg.last_name = input("Enter your last name: ")
    user_reg.email = input("Enter your email: ")
    user_reg.mobile_number = input("Enter your mobile number: ")
    user_reg.password = input("Enter your password: ")

    user_reg.First_name()
    user_reg.Last_name()
    user_reg.email_validation()
    user_reg.mobile_valid()
    user_reg.password_validation()
