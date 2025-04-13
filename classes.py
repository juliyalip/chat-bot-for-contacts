from collections import UserDict
import validations


class Field:
    def __init__(self, value: str):
        self.value = value

    def _validate(self, value):
        pass

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._validate(new_value)
        self._value = new_value
    
    def __str__(self):
        return str(self.value)
    
# Name 
class Name(Field):
    def _validate(self, name):
        validations.is_valid_name(name) 

# Phone  
class Phone(Field):
    def _validate(self, phone):
       validations.is_valid_phone(phone)

# Birthday
class Birthday(Field):
    def _validate(self, date):
        validations.is_valid_date_format(date)
    
# Phonebook

  



   
        



class Record:
    def __init__(self, name: str):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        pass

# phonebook

class AdressBook(UserDict):
    pass





