from collections import UserDict
import uuid
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

# Record
class Record:
    def __init__(self, name: str, ):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.id = str(uuid.uuid4())

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def set_birthday(self, date: str):
        self.birthday = Birthday(date)

    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if old_phone == phone.value:
                validated_phone = Phone(new_phone)
                phone.value = validated_phone.value
                return "The phone was updated"
        else:
            return "The phone was not found"
            
    def __str__(self):
        phones=", ".join(str(phone) for phone in self.phones)
        return f"name: {self.name}, phones: {phones}, birthday: {self.birthday if self.birthday else "not set"}"



# Phonebook
class Phonebook(UserDict):
    def add_record(self, record):
        self.data[record.id] = record
        return "contact was added"
    
    def find_records(self, name:str):
        contacts=[]
        for record in self.data.values():
            if name.lower() == record.name.value.lower():
                contacts.append(record)
        if not contacts:
            raise KeyError("The contact was not found")
        return contacts
    
    def delete_record(self, name: str):
        record = self.find_record(name)
        del self.data[record.id]
        return f"The contact {name} was deleted"
    
    def __str__(self):
        if not self.data:
            return "You don't have any records."
        return "\n".join(str(record) for record in self.data.values())
   






        












