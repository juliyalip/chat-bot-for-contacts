import handlers

commands = {
    "add": ("add contact", handlers.add_contact),
    "show_all": ("list contacts", handlers.show_all),
    "search_contact": ("search contact", handlers.search_contact),
    "delete_contact": ("delete contact", handlers.delete_contact),
    "exit": ('exit' , None)
}