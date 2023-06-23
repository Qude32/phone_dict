def add_contact(name_contact, phone_num, cont_dict):
    cont_dict[name_contact] = phone_num
    return cont_dict


def search(cont_surname, cont_dict):
    temp_dict = {}
    for surname, number in cont_dict.items():
        if cont_surname in surname:
            temp_dict[surname] = number
    if temp_dict:
        return temp_dict
    else:
        return 0


def delete_contact(d_contact, cont_dict):
    if d_contact not in cont_dict:
        return 'Такого контакта в записной книжке нет!'
    else:
        cont_dict.pop(d_contact)
        return f'Контакт "{" ".join(d_contact)}" успешно удален! \nТекущий список контактов: {cont_dict}'


def main():
    contacts_dict = {}
    while True:
        print('\nВведите номер действия: '
              '\n1. Добавить контакт' 
              '\n2. Найти человека '
              '\n3. Удалить контакт')
        choice = int(input())
        if choice == 1:
            name = input('\nВведите имя и фамилию нового контакта (через пробел): ').title().split()
            name = tuple(name)
            if name not in contacts_dict:
                phone_number = int(input('Введите номер телефона: '))
                print(f'\nТекущий словарь контактов: {add_contact(name, phone_number, contacts_dict)}')
            else:
                print('\nТакой человек уже есть в контактах.')
                print(f'Текущий словарь контактов: {contacts_dict}')
        elif choice == 2:
            surname = input('Введите фамилию для поиска: ').title()
            result = search(surname, contacts_dict)
            if result:
                for person, number in result.items():
                    print(f'{" ".join(person)} {number}')
            else:
                print('Такого человека нет в контактах.'
                      f'\nТекущий словарь контактов: {contacts_dict}')
        elif choice == 3:
            del_contact = input('Введите имя и фамилию контакта, '
                                'который следует удалить (через пробел): ').title().split()
            print(delete_contact(tuple(del_contact), contacts_dict))


main()
