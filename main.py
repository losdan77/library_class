import json
import time

class Book:
    def __init__(self, 
                 title: str, 
                 author: str,
                 year: int):
        '''Иницилизация обьекта "Книга" и добавление ее в общий json,
        если json не создан, создает его'''

        self.id = int(round(((time.time())%100000), 3)*10000)
        self.title = title
        self.author = author
        self.year = year
        self.status = 'в наличии'
        
        book_dict = {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'status': self.status
        }
        library_mass = []

        with open('library.json', 'r', encoding='utf-8') as file:
            try:
                library_json = json.load(file)
                for _ in library_json:
                    library_mass.append(_)
            except:
                pass
        
        library_mass.append(book_dict)

        with open('library.json', 'w', encoding='utf-8') as file:
            json.dump(library_mass, file, ensure_ascii=False, indent=4)

    @staticmethod
    def delete_book(id: int):
        '''Поиск книги по id и удаление по значению элемента массива'''

        find_book = False

        with open('library.json', 'r', encoding='utf-8') as file:
            library_json = json.load(file)
        
        for book in library_json:
            if book['id'] == id:
                library_json.remove(book)
                find_book = True
        
        with open('library.json', 'w', encoding='utf-8') as file:
            json.dump(library_json, file, ensure_ascii=False, indent=4)

        return find_book

    @staticmethod
    def search_book(find_key: str, find_value: str):
        '''Поиск книги по выбранному значению словаря и точному совпадению 
        значения ключа словаря, выводятся все совпадения в новом массиве'''
        
        book_mass = []
        find_book = False

        with open('library.json', 'r', encoding='utf-8') as file:
            library_json = json.load(file)

        for book in library_json:
            if str(book[find_key]) == str(find_value):
                book_mass.append(book)
                find_book = True

        if find_book:
            for book in book_mass:
                print(book)
            time.sleep(1.0)
        else:
            print('WARNING: По вашему запросу нет книг!')
            time.sleep(1.0)

    @staticmethod
    def select_all_books():
        '''Вывод всех значений из json'''

        with open('library.json', 'r', encoding='utf-8') as file:
            library_json = json.load(file)

        for book in library_json:
            print(book)

        time.sleep(1.0)

    @staticmethod
    def change_status_book(id: int):
        '''Находит книгу по id и инвертирует значение status'''

        with open('library.json', 'r', encoding='utf-8') as file:
            library_json = json.load(file)
        
        find_book = False
        for book in library_json:
            if book['id'] == id:
                if book['status'] == 'в наличии':
                    book['status'] = 'выдана'
                else:
                    book['status'] = 'в наличии'
                find_book = True
        
        with open('library.json', 'w', encoding='utf-8') as file:
            json.dump(library_json, file, ensure_ascii=False, indent=4)

        return find_book

if __name__ == "__main__":
    menu_dict = {
            1: 'Добавить книгу',
            2: 'Удалить книгу',
            3: 'Поиск книги',
            4: 'Вывести все книги',
            5: 'Изменить статус книги',
            6: 'Выход из программы'
        }
    signal = True

    '''Благодаря циклу программа выполняется до того пока пользователь не закрое ее'''
    while signal:      
        print('Выберите пункт меню:')
        for number, value in menu_dict.items():
            print(f'{number}) {value}') 

        '''С помощью конструкции try except выполняется общая проверка, 
        на то чтобы пользователь вводил число или цифру (int)'''
        try:
            user_number = int(input('>'))
            
            '''Закрыть программу'''
            if user_number == 6:
                signal = False

            '''Проверка на то, чтобы пользователь вводил значения представленные в меню'''
            if user_number not in menu_dict:
                print('WARNING: Такого пункта меню не существует!')
                time.sleep(1.0)
            
            if user_number == 1:
                title = input('Название книги:')
                author = input('ФИО автора:')
                year = int(input('Год:'))
                book = Book(title = title,
                            author = author,
                            year = year,)
                print('INFO: Книга создана!')
                time.sleep(1.0)

            if user_number == 2:
                try:
                    book_id = int(input('Введите id книги:'))
                    result = Book.delete_book(id=book_id)
                    if result:
                        print(f'INFO: Книга {book_id} удалена!')
                        time.sleep(1.0)
                    else:
                        print(f'WARNING: Книги  с id={book_id} не существует!')
                        time.sleep(1.0)
                except:
                    print('WARNING: Введите пожалуйста число!')
                    time.sleep(1.0)

            if user_number == 3:
                find_key_dict = {
                    1: 'title',
                    2: 'author',
                    3: 'year'
                }
                print('1) По названию')
                print('2) По автору')
                print('3) По году выпуска')
                number_find_key = int(input('Выберите по какому полю искать:'))
                if number_find_key not in find_key_dict:
                    print('WARNING: Такого варианта ответа не существует!')
                    time.sleep(1.0)
                else:
                    find_value = input('Введите по какому значению искать:')
                    Book.search_book(find_key=find_key_dict[number_find_key],
                                     find_value=find_value)

            if user_number == 4:
                Book.select_all_books()
                time.sleep(1.0)

            if user_number == 5:
                try:
                    book_id = int(input('Введите id книги:'))
                    result = Book.change_status_book(id=book_id)
                    if result:
                        print(f'INFO: Статус книги {book_id} изменен!')
                        time.sleep(1.0)
                    else:
                        print(f'WARNING: Книги  с id={book_id} не существует!')
                        time.sleep(1.0)
                except:
                    print('WARNING: Введите пожалуйста число!')
                    time.sleep(1.0)
        
        except:
            print('WARNING: Введите пожалуйста число!')
            time.sleep(1.0)

        