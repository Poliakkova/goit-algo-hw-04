"""
Ваше завдання - розробити функцію get_cats_info(path),
яка читає цей файл та повертає список словників з інформацією
про кожного кота.
"""


from colorama import Fore, Style

def get_cats_info(path):
    list_of_cats = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):

                try:
                    id, name, age = line.split(',')
                except ValueError:
                    print(Fore.YELLOW + f"Wrong format! Line {i+1} skipped" + Style.RESET_ALL)
                    continue

                list_of_cats.append({'id': id.strip(),
                                     'name': name.strip(),
                                     'age': age.strip()})
    except FileNotFoundError:
        print(Fore.RED + f"Error! File {path} not found" + Style.RESET_ALL)

    return list_of_cats

if __name__ == '__main__':
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
