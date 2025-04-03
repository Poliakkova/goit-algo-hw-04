"""
Ваше завдання - розробити функцію total_salary(path),
яка аналізує цей файл і повертає загальну та середню суму
заробітної плати всіх розробників.
"""


from colorama import Fore, Style

def total_salary(path):
    """
    Returns total and average salary
    :param path: str
    :return: tuple total_salaries, average_salary
    """

    total_salaries = 0
    average_salary = 0
    number_of_valid_data = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):

                try:
                    _, salary = line.split(',', 1)
                    total_salaries += int(salary)
                    number_of_valid_data +=1
                except ValueError:
                    print(Fore.YELLOW + f"Wrong format! Line {i+1} skipped" + Style.RESET_ALL)
                    continue

            average_salary = total_salaries / number_of_valid_data
    except FileNotFoundError:
        print(Fore.RED + f"Error! File {path} not found" + Style.RESET_ALL)
    return total_salaries, average_salary

if __name__ == '__main__':
    total, average = total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
