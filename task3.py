"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка
 і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів.
 Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.
"""

import sys
from colorama import Fore, Style
from pathlib import Path


def show_directory_structure(path_str, level=0):
    """
    Shows directory structure
    :param path_str: path to directory
    :param level: length of spaces
    :return:
    """
    path = Path(path_str)
    spaces = 4*' '

    if path.is_dir():
        print(Fore.BLUE + level * spaces + '📂' + path.name + '/' + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Error! Path {path} is a file, not a directory" + Style.RESET_ALL)
        return

    try:
        for element in path.iterdir():
            # якщо елемент папка, викликаємо функцію рекурсивно, додаючи відступ на початку
            if element.is_dir():
                show_directory_structure(element, level+1)

            # якщо елемент файл, друкуємо з відступом
            if element.is_file():
                icon = ''
                element_type = element.suffix
                match element_type:
                    case '.txt' | '.doc' | '.docx' | '.pdf':
                        icon = '📝'
                    case '.zip' | '.tar' | '.gz':
                        icon = '🗂'
                    case '.png' | '.jpg':
                        icon = '🖼'
                    case '.xlsx':
                        icon = '📊'
                    case '.pptx':
                        icon = '🪧'
                    case _:
                        icon = '📄'

                print(Fore.GREEN + (level+1) * spaces + icon + element.name + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + f"Error! Path {path} not found" + Style.RESET_ALL)


if __name__ == '__main__':
    show_directory_structure(sys.argv[1])
    # (.venv) anastasiapolakova@MacBook-Air-Anastasia goit-algo-hw-04 % python3 task3.py /Users/anastasiapolakova/Study/repository_destination/goit-algo-hw-04/temp