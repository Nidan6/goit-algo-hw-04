def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: add [name] [phone]"

    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command format. Use: change [name] [new_phone]"

    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return f"Contact {name} updated."
    else:
        return f"Contact {name} not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command format. Use: phone [name]"

    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return f"Contact {name} not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
        else:
            print("Вийшло у Вас не дуже. І цього не варто було робити, краще взагалі навіть не намагатися зробити якось з більшим використанням знань з уроків, бо чудовий ментор навіть не спробує допомогти чи підказати як зробити правильно :)")


if __name__ == "__main__":
    main()