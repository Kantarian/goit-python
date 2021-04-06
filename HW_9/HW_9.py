users = {
    'qwe' :'+3809756786',
    'asd':'+38066321245'
}

def input_error(func, name = 'empty', phone_number = 'No number'):
    if func.__name__ == 'add_new':
        return f'{name} already in contacts'
    if func.__name__ == 'change':
        return f'{name} not in contacts'
    if func.__name__ == 'phone':
        return f'{name} not in contacts'        
    else:
        return ('something went wrong please try again (:')

def hello():
    return "How can I help you?"

def add_new(name = 'empty', phone_number = 'No number'):
    users[name] = phone_number
    return f'user {name} with phone number {phone_number} was add'

def change(name = 'empty', phone_number = 'No number'):
    users[name] = phone_number
    return f'user {name} with new phone number {phone_number}'

def phone(name = 'empty'):
    phone_number = users[name]
    return f'user {name} phone number {phone_number}'

def show_all():
    dictionary_items = users.items()
    name_num = ''
    for item in dictionary_items:   
        name_num = name_num + str(item)
    return name_num

def help_bot():
    return '''
    Бот принимает команды:
    "hello", отвечает в консоль "How can I help you?"
    "add ...". По этой команде бот сохраняет в памяти (в словаре например) новый контакт.
    "change ..." По этой команде бот сохраняет в памяти новый номер телефона для существующего контакта.
    "phone ...." По этой команде бот выводит в консоль номер телефона для указанного контакта.
    "show all". По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
    "good bye", "close", "exit" по любой из этих команд бот завершает свою роботу после того, как выведет в консоль "Good bye!". '''

def main():
    a = 1
    while a:
        input_word = input('Hi I\'m bot, write something: ' ).lower()
        stop = ('.','good bye','close','exit')
        if input_word not in stop:
            if input_word == 'hello':
                print(hello())
                continue
            if input_word == 'add':
                b = 1
                while b:
                    name = str(input('add name: ')).lower()
                    if name in users:
                        print (input_error(add_new, name))                        
                    else:
                        phone_number = str(input('add phone number: ')).lower()
                        print (add_new(name, phone_number))
                        b = 0
                else:
                    continue
            if input_word == 'change':
                b = 1
                while b:
                    name = str(input('name in contacts: ')).lower()
                    if name not in users:
                        print (input_error(change, name))                        
                    else:
                        phone_number = str(input('add new phone number: ')).lower()
                        print (change(name))
                        b = 0
                else:
                    continue
            if input_word == 'phone':
                b = 1
                while b:
                    name = str(input('name in contacts: ')).lower()
                    if name not in users:
                        print (input_error(phone, name))                        
                    else:
                        print (phone(name))
                        b = 0
                else:
                    continue
            if input_word == 'show all':
                print(show_all())
                continue
            if input_word == 'help':
                print(help_bot())
            else:
                print (input_error(main)) 
        else:
            a = 0
    else:
        print('Good bye!')


if __name__ == '__main__':
    main()