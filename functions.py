# r - только чтение файла
# a - дозапись в файл
# w - перезапись файла

def show_data() -> None:
    """Выводит информацию из справочника"""

    with open('sem_8_practice\\book.txt', 'r', encoding='utf-8') as book:
        print(book.read())
# вместо book.txt вставить относительный адрес файла - правой кнопкой мыши на book.txt -> 
# copy relative path 

def add_data() -> None:
    """Добавляет информацию в справочник."""
    fio = input('Введите ФИО: ')
    phone_num = input('Введите номер телефона: ')
    with open('sem_8_practice\\book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{fio} | {phone_num}')
        

def find_data() -> None:
    """Печатает результат поиска по справочнику."""
    with open('sem_8_practice\\book.txt', 'r', encoding='utf-8') as file:
        data = file.read()
    contact_to_find = input('Введите, что хотите найти: ')    
    result = search(data, contact_to_find)
    print(result)

# # def search(book: str, info: str) -> list[str]:
#     """Находит в списке записи по определенному критерию поиска"""
#     book = book.split('\n')
#     return list(filter(lambda contact: info.lower() in contact.lower(), book))
# book = book.split('\n')
#     return list(filter(lambda contact: info.lower() in contact.lower(), book))

# def search(book: str, info: str) -> list[str]:
def search(book: list[str], info: str) -> list[str] | str:
    result = [contact for contact in book if info in contact]
    if not result:
        return "Совпадений не найдено"
    elif len(result) == 1:
        return result[0]
    elif len(result) > 1:
        print()
        print('--------------')
        print('\n'.join(result))
        new_info = input('Введите данные для поиска: ')
        print(search(data, data_to_find))

def change() -> None:
    """Изменение/удаление данных в справочнике."""
    with open('book.txt', 'r', encoding='utf-8') as file:
        data = file.read().split('\n')
    print('\n'.join(data))
    data_to_edit = input('Введите данные для поиска: ')
    data_to_edit = search(data, data_to_edit)
    mode = input('Удалить или изменить? 1 - удалить, 2 - заменить')
    if mode == '1':
        data.remove(data_to_edit)
    elif mode == '2':
        data(data.index(data_to_edit)) == enter_contact()

    with open('book.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(data))

def enter_contact() -> str:
    fio = input('Введитте ФИО: ')
    phone = input('Введите номер телефона: ')
    return f'{fio} | {phone}'
    


