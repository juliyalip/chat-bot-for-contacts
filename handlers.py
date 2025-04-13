from classes import Phonebook

INDENT = 11
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return f"{' ' * INDENT} Give me a name and a phone please."
        except KeyError:
            return f"{" " * INDENT}Contact does not exist in your contact list"
        except IndexError:
            return f"{' ' * INDENT}Enter the argument for the command"
        except Exception as e:
            return f"{' ' * INDENT}{str(e)}"
    return inner

# custom input
def safe_input(prompt: str, allow_empty = False):
    indented_prompt = " " * INDENT + prompt
    user_input = input(f"{indented_prompt}('/' to main menu): ").strip()

    if user_input=='/':
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
    name = safe_input("")

def show_all():
    pass

def search_contact():
    pass

def delete_contact():
    pass


