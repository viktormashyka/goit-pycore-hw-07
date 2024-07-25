from functools import wraps

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Invalid input. Please provide the correct information."
        except Exception as e:
            return f"An error occurred: {e}"

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        print("Name and phone number are missing.")
        raise ValueError
    name, phone = args
    contacts[name] = phone
    return f"Contact with name {name} added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        print("Name and phone number are missing.")
        raise ValueError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return f"Contact with name {name} changed."

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        print("Name is missing.")
        raise ValueError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return (contacts.get(name))

@input_error
def show_all(contacts):
    if not contacts:
        print("No contacts found")
    return (contacts)

@input_error
def help():
    print("\thello - start dialog")
    print("\tadd <name> <phone> - add contact, require name and phone")
    print("\tchange <name> <phone> - change contact, require name and new phone")
    print("\tphone <name> - show phone, require name")
    print("\tall - show all contacts")
    print("\texit or close - exit")

def main():
    contacts = {}
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
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help" or "-h":
            help()
        else:
            print("Invalid command.")
        

if __name__ == "__main__":
    main()
    
# Приклад використання:
# Welcome to the assistant bot!
# Enter a command: test
# Invalid command.
# Enter a command: hello
# How can I help you?
# Enter a command: add Mike 0501111111
# Contact added
# Enter a command: change Mike 0502222222
# Contact changed
# Enter a command: phone Mike
# 0502222222
# Enter a command: all
# {"Mike":"0502222222"}
# Enter a command: exit
# Good bye!
