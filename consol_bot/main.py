#  З попереднього боту прибрав всі блоки try...except

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"
        except KeyError:
            return "Error: Contact not found."

    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# "add username phone" --> add contact
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

# "change username phone" --> change contact phone
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] 
    return "Contact not found."

# "phone username" --> show contact phone
@input_error
def show_contacts(args, contacts):
    name = args[0]
    return f"{name}: {contacts[name]}"



# "all" --> show all contacts
@input_error
def show_all_contacts(contacts):
    if not contacts:
        return "No contacts found."

    phones = []
    for name, phone in contacts.items():
        phones.append(f"{name}: {phone}")
    return "\n".join(phones)



def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        # "close", "exit" -->  "Good bye!"
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        # "hello"--> "How can I help you?"
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contacts(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()