#!/usr/bin/python3
""" User class """


import hashlib


class User:
    """ User class """

    def __init__(self):
        """ Initialize User """
        self.password = None

    @property
    def password(self):
        """ Password getter """
        return self.__password

    @password.setter
    def password(self, pwd):
        """ Password setter """
        if pwd is None:
            self.__password = None
        elif isinstance(pwd, str):
            self.__password = hashlib.md5(pwd.encode()).hexdigest()
        else:
            raise TypeError("password must be a string")

    def is_valid_password(self, pwd):
        """ Check if password is valid """
        if pwd is None:
            return False
        if self.password is None:
            return False

        return hashlib.md5(pwd.encode()).hexdigest() == self.password

