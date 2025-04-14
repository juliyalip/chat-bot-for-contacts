from classes import Phonebook, Record

INDENT = 11
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{' ' * INDENT} Give me a name and a phone please."
        except KeyError:
            return f"{' ' * INDENT}Contact does not exist in your contact list"
        except IndexError:
            return f"{' ' * INDENT}Enter the argument for the command"
        except Exception as e:
            return f"{' ' * INDENT}{str(e)}"
    return inner

# custom input
def safe_input(prompt: str, allow_empty = False):
    indented_prompt = " " * INDENT + prompt
    user_input = input(f"{indented_prompt}('/' to main menu): ").strip()

    if user_input == '/':
        print(' '* INDENT + 'Operation cancelled')
        return None
    if not user_input and not allow_empty:
        print(" " * INDENT + "This file cannot be empty. Please try again or type '/' to return to menu")
        return safe_input(prompt, allow_empty)
    
    return user_input

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(book: Phonebook):
    name = safe_input("Enter a contact name")
    if name is None:
        return ""
    
    record = Record(name)
    while True:
        phone = safe_input("Enter a phone: ", allow_empty=True)
        if phone is None:
            return ""  
        if not phone:
            break
        try:
            record.add_phone(phone)
            break
        except ValueError as e:
            print(f"{' ' * INDENT}{e}")

    birthday = safe_input("Enter a birthday: ", allow_empty=True)   
    if birthday is None:
        return ""
    if birthday:
        try:
           record.birthday = birthday
        except ValueError as e:
            return " " * INDENT + str(e)
        
    try:
        book.add_record(record)
        return " " * INDENT + "Contact was added"
    except KeyError as e:
        return " " * INDENT + str(e)


def show_all(book: Phonebook):
    if book:
        return book
    else:
        return " " * INDENT + "You don't have any contacts"
       

@input_error
def search_contact(book: Phonebook):
    name=safe_input("Enter name to find: ", allow_empty=True)
    if name is None:
        return ""
    return book.find_records(name)


@input_error
def change_contact(book: Phonebook):
    name = safe_input("Enter name: ", allow_empty=False)
    if name is None:
        return ""
    records = book.find_records(name)

    if len(records) > 1:
       print("Found multiple contacts:")
       for idx, record in enumerate(records, 1):
            print(f"{idx}: {record}")
       contact_index = safe_input("Enter witch one do you want to chose: (use number 1, 2, ..) ", allow_empty=False)
       if contact_index is None:
           return ''
       try:
           index = int(contact_index)-1
           if index < 0 or index >= len(records):
               return f"{' ' * INDENT}Invalid selection"
           record = records[index]
       except ValueError:
           return f"{' ' * INDENT}Invalid input. Please enter a number"
       
    else:
        record=records[0]

    choice =safe_input("To change the name enter(1), to  the phone enter (2): ").strip()
    if choice is None:
        return ''
    
    if choice =='1':
        new_name = safe_input("Enter the new name: ", allow_empty=False)
        if new_name is None:
            return 'The name was not changet'
        try:
            record.name.value = new_name
            return "The name was updated"
        except KeyError as e:
            return f"{e}"
    elif choice =='2':
        phones = safe_input("Enter the old phone and the new phone - sparated coma: ", allow_empty=False).strip()
        if phones is None:
            return ''
        try:
             old_phone, new_phone = phones.split(',')
             return record.edit_phone(old_phone, new_phone.strip())
        except ValueError as e:
            return f"{e}"
    return f"{' ' * INDENT} Invalid choice"


@input_error
def delete_contact(book: Phonebook):
    name = safe_input("Enter name to delete ", allow_empty=False)
    if name is None:
        return ''
    if name:
        confirmation = safe_input("Do you want to delete? (y/n) ", allow_empty=False).lower()
        if confirmation is None or confirmation == 'n':
            return f"{' ' * INDENT}Deleteion was canceled"       
        book.delete_record(name)
        return f"{' ' * INDENT}Contact was deleted"
    





