import pickle
from classes import Phonebook


class EmptyFileError(Exception):
    pass

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            f.seek(0)
            first_bytes = f.read(1)
            if not first_bytes:
                raise EmptyFileError
            f.seek(0)
            return pickle.load(f)
    except(FileNotFoundError, EmptyFileError):
        return Phonebook()