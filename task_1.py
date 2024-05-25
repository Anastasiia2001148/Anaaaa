from collections import UserDict
import datetime
import pickle

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        assert len(str(self.value)) == 10, 'Number is too short'

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [i for i in self.phones if i.value != phone]

    def edit_phone(self, new, old):
        for i in self.phones:
            if i.value == old:
                i.value = new

    def find_phone(self, phone):
        return [i for i in self.phones if i.value == phone]

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        return self.data.pop(name)

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.datetime.strptime(value, '%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class InputError(Exception):
    pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InputError as e:
            return str(e)
        except AssertionError:
            print('Number too  short')
        except ValueError:
            print('ValueError')
    return inner

class RecordBook(AddressBook):
    @input_error
    def add_birthday(self, args):
        name, birthday = args
        record = self.find(name)
        if record:
            record.birthday = Birthday(birthday)
            return f"Birthday added for {name}."
        else:
            raise InputError("Contact not found.")

    @input_error
    def show_birthday(self, args):
        name = args[0]
        record = self.find(name)
        if record and record.birthday:
            return f"{name} has birthday on {record.birthday.value.strftime('%d.%m.%Y')}."
        else:
            raise InputError("Birthday not found.")

    @input_error
    def birthdays(self, _):
        today = datetime.datetime.now()
        next_week = today + datetime.timedelta(days=7)
        upcoming_birthdays = [name for name, record in self.data.items() if record.birthday and today < record.birthday.value < next_week]
        return f"Upcoming birthdays: {', '.join(upcoming_birthdays)}"

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()  # Повернення нової адресної книги, якщо файл не знайдено

def main():
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            name, phone = args
            book.add_record(Record(name))
            book[name].add_phone(phone)
            print(f"Contact {name} added with phone {phone}.")

        elif command == "change":
            name, new_phone, old_phone = args
            book[name].edit_phone(new_phone, old_phone)
            print(f"updated for {name}.")

        elif command == "phone":
            name = args[0]
            phones = [str(phone) for phone in book[name].phones]
            print(f"Phone numbers for {name}: {', '.join(phones)}")

        elif command == "all":
            for name, record in book.data.items():
                print(record)

        elif command == "add-birthday":
            book.add_birthday(args)
            print("Birthday added.")

        elif command == "show-birthday":
            print(book.show_birthday(args))

        elif command == "birthdays":
            print(book.birthdays(args))

        else:
            print("Invalid command.")



if __name__ == "__main__":
    main()