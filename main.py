import commands
from classes import AdressBook

def main():

    def print_menu():
        print("\nMenu")
        print("-" * 30)
        for key, (desc, _) in commands.commands.items():
             print(f"{key :<15} : {desc: <20}") 

    while True:
        print_menu()
        choice= input("Enter your choice: ").strip()
        if choice in ["close", "exit"]:
            print("Good bye!")
            #save_data(book)
            break
        if choice not in commands:
            print("Invalid selection. Try again.")
            continue
        desc, handler = commands[choice]
        if choice == "exit":
            print("Data saved. Goodbay")
            # save data
            break

        target_book = AdressBook()

        result = handler(target_book)

        if result:
            print(result)

if __name__=="__main__":
    main()