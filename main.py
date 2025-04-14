from classes import Phonebook
from api_handlers import save_data, load_data
import handlers

def main():
     
    book=load_data()

    def print_menu(_=None):
        print("\nMenu")
        print("-" * 30)
        for key, (desc, _) in commands.items():
             print(f"{key :<15} : {desc: <20}") 

    commands = {
    "add": ("add contact", handlers.add_contact),
    "all": ("list contacts", handlers.show_all),
    "search": ("search contact", handlers.search_contact),
    "change" : ("change contact",  handlers.change_contact),
    "delete": ("delete contact", handlers.delete_contact),
    "help": ("help", print_menu),
    "exit": ('exit & save' , None)
    }

    print("Welcome to the assistant bot!")
    print(print_menu())         
    while True:
        choice= input("Enter your command: ").strip()
        if choice not in commands:
            print("Invalid selection. Try again.")
            continue

        desc, handler = commands[choice]
        if choice in ["close", "exit"]:   
            save_data(book)
            print("Data saved. Good bye!")
            break
        
        result = handler(book)
        if result:
            print(result)

if __name__=="__main__":
    main()