contacts= {}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print('Contact updated')
    else:
        print('Name not found')

def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print('Contact not found')

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
            print(add_contact(args, contacts))
        elif command == 'change':
            (change_contact(args[0],args[1]))
        elif command == 'phone':
            (show_phone(args[0]))
        elif command == "all":
            show()
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
