contacts= {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Key Error"
        except IndexError:
            return 'Index Error'
        except TypeError:
            return 'Type Error'
    return inner
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    print("Contact added.")
@input_error
def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print('Contact updated')
    else:
        print('Name not found')
@input_error
def show_phone(name, contacts):
    if name in contacts:
        print(contacts[name])
    else:
        print('Contact not found')

@input_error
def show():
    for name, phone in contacts.items():
        print(f'{name}:{phone}')


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            (add_contact(args, contacts))
        elif command == 'change':
            (change_contact(*args))
        elif command == 'phone':
            (show_phone(*args, contacts))
        elif command == "all":
            show()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()