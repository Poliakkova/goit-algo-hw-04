"""
Напишіть консольного бота помічника, який розпізнаватиме команди, що вводяться з клавіатури,
та буде відповідати згідно із введеною командою.

На першому етапі наш бот-асистент повинен вміти зберігати ім'я та номер телефону,
знаходити номер телефону за ім'ям, змінювати записаний номер телефону,
виводити в консоль всі записи, які зберіг. Щоб реалізувати таку нескладну логіку, скористаємося словником.
У словнику будемо зберігати ім'я користувача, як ключ, і номер телефону як значення.
"""


import colorama

colorama.init(autoreset=True)

def start_bot():
    print(colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX +
          "Welcome to bot-assistant 📞Phone Book📞! What can I help you with? 😊")
    show_help()

    contacts = {}

    while True:
        input_str = input(">> ").strip().lower()
        if input_str == '':
            continue

        command, *args = parse_input(input_str)

        if command in ('exit', 'close'):
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'help':
            show_help()
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(find_contact(args[0], contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print(colorama.Fore.YELLOW + "⚠️ It's not a command. Type 'help' to see available commands")

    print(colorama.Style.BRIGHT + colorama.Fore.LIGHTYELLOW_EX +
          "Good bye! 😊")


def parse_input(input_str: str):
    command, *args = input_str.split()
    command = command.strip().lower()
    return command, *args


def show_help():
    print("Command list:")
    print("\tadd [name] [phone number]        | add new name and phone number")
    print("\tphone [name]                     | find phone number by person's name")
    print("\tchange [name] [new phone number] | edit phone number by person's name")
    print("\tall                              | show all phone numbers")
    print("\thelp                             | if you need to see this commands again")
    print("\texit / close                     | to close bot-assistant")


def change_contact(args, contacts:dict):
    try:
        name, phone = args
        if contacts.get(name):
            contacts[name] = phone
            return colorama.Fore.GREEN + '✅ Contact changed!'
        else:
            while True:
                print(colorama.Fore.YELLOW + f"⚠️ Contact with name '{name}' not found. Create new contact?")
                print("yes - create contact\n"
                      "no - return to main menu")

                answer = input('>> ').strip().lower()
                if answer == 'yes':
                    contacts[name] = phone
                    return colorama.Fore.GREEN + '✅ Contact added!'

                elif answer == 'no':
                    return "Main menu. Type 'help' to see available commands"

                else:
                    print(colorama.Fore.YELLOW + "⚠️ Sorry, I don't understand")


    except ValueError:
        return colorama.Fore.RED + "🔴 Error! Not enough arguments. Must be: edit [name] [phone number] "


def add_contact(args, contacts:dict):
    try:
        name, phone = args
        if contacts.get(name):
            while True:
                print(colorama.Fore.YELLOW + f"⚠️ Contact with name '{name}' already exists. Number: {contacts.get(name)}. Do you want to overwrite it?")
                print("yes - overwrite\n"
                      "no - enter new name\n"
                      "skip - return to main menu")

                answer = input('>> ').strip().lower()
                if answer == 'yes':
                    contacts[name] = phone
                    return colorama.Fore.GREEN + '✅ Contact changed!'

                elif answer == 'no':
                    new_name = input("Enter new name: ")
                    contacts[new_name] = phone
                    return colorama.Fore.GREEN + '✅ Contact added!'

                elif answer == 'skip':
                    return "Main menu. Type 'help' to see available commands"

                else:
                    print(colorama.Fore.YELLOW + "⚠️ Sorry, I don't understand")

        contacts[name] = phone
        return colorama.Fore.GREEN + '✅ Contact added!'
    except ValueError:
        return colorama.Fore.RED + "🔴 Error! Not enough arguments. Must be: add [name] [phone number] "


def find_contact(name, contacts:dict):
    try:
        return f"{name}: {contacts[name]}"
    except KeyError:
        return colorama.Fore.RED + f"🔴 Contact with name '{name}' not found"


def show_all(contacts:dict):
    print("All contacts:")
    for i, (name, phone) in enumerate(contacts.items()):
        print(f"{i+1}. {name}: {phone}")


if __name__ == '__main__':
    start_bot()