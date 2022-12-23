import view

phone_book = []


def get_phone_book() -> list:
    global phone_book
    return phone_book


def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book


def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)


def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id - 1][0]}? (y/n) ')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id - 1)


def find_contact():
    global phone_book
    find_string = view.input_find()
    not_find = True
    for id, contact in enumerate(phone_book):
        for item in contact:
            if find_string in item.lower():
                not_find = False
                print((id + 1), *contact)
    if not_find:
        print('Такого контакта нет.')


def change_contact():
    global phone_book
    id = view.input_change_contact()
    print(*phone_book[id - 1])
    confirm = input(f'Вы точно хотите изменить контакт {phone_book[id - 1][0]} (y/n)? (yes/no) ')
    if confirm.lower() == 'yes':
        del_contact = phone_book.pop(id - 1)
        change_contact = view.input_new_contact()
        phone_book.insert(id - 1, change_contact)
        print('Контакт был изменен: ', end='')
        print(*phone_book[id - 1])
