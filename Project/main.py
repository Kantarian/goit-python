import contact_book
import sort_file
import Noter
import inspect
import pathlib
import signal
import sys


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            return f'Command {e} not found!!!'
        except ValueError as e:
            return e
        except IndexError as e:
            return f'Command not full!!'
    return inner


def com_add(name, phone, email = None, birthday=None):
    if name.value in [key.value for key in list(contact_list.keys())]:
        raise ValueError(f'The new contact cannot be saved because the name "{name.value}" already exists. '
                         f'Please enter a different name.\n')

    record = contact_book.Record(name, birthday) + phone + email
    contact_list.add_record(name, record)
    return f'New contact is saved: name "{name.value}", phone "{phone.value}",'\
        f'email "{email.value if email else "-"}",'\
        f' date of birth "{birthday.value if birthday else "-"}".\n'

            
def com_change(name, phone, new_phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(
            f'Сontact by name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            for ph in rec.phones:
                if ph.value == phone:
                    rec.change_phone(ph, new_phone)
                    return f'Saved a new phone number "{new_phone.value}" for a contact with the name "{name}".\n'
                else:
                    raise ValueError(
                        f'The contact "{name}" does not have a phone number {phone}.\n')


def com_exit():
    return 'Good bye!\n'


def com_hello():
    return 'How can I help you?\n'


def com_join(name, phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(
            f'Сontact with name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            record = rec + phone
            contact_list.add_record(nam, record)
    return f'A new phone number "{phone.value}" has been added for the contact with the name "{name}".\n'


def com_delete(name, phone):
    if not name in [key.value for key in list(contact_list.keys())]:
        raise ValueError(
            f'Сontact by name "{name}" does not exist. Enter the correct name.\n')
    for nam, rec in contact_list.items():
        if nam.value == name:
            for ph in rec.phones:
                if ph.value == phone:
                    rec.remove(ph)
                    return f'Delete phone number "{phone.value}" for a contact with the name "{name}".\n'
                else:
                    raise ValueError(
                        f'The contact "{name}" does not have a phone number {phone}.\n')


def com_phone(name):
    for nam, rec in contact_list.items():
        if nam.value == name:
            return ' '.join([phone.value for phone in rec.phones])
    raise ValueError(f'Contact with the name "{name}" does not exist.\n')


def com_show_all():
    return contact_list.iterator()


def com_search(pattern):
    result = ''
    for nam, rec in contact_list.items():
        phone_list = [phone.value for phone in rec.phones]
        for p in phone_list:
            if p.find(pattern) != (-1) or nam.value.find(pattern) != (-1):
                result += f'name: {nam.value}, phone: {" ".join([phone.value for phone in rec.phones])}, ' \
                          f'birtday: {rec.birthday.value if rec.birthday else "-"} ' \
                          f'{"("+str(rec.days_to_birthday())+" days)" if rec.days_to_birthday() else ""}\n'
    if not result:
        raise ValueError(f'No matches.\n')
    return result


@ input_error
def get_command_handler(user_input):
    if user_input[:2] == ['show', 'all']:
        return com_show_all()
    
    if user_input[:2] == ['contact', 'book']:
        print(com_hello())
        while True:
            user_input = input(
                'Enter your command (add, join, change, phone, search, delete, show all or exit/close/good bye):\n').lower().split() 
            
            if user_input[:2] == ['good', 'bye'] or user_input[0] in ('close', 'exit'):
                return com_exit()
            
            if user_input[0] == 'search':
                user_input = input(
                'Enter what search: \n').split()
                return com_search(user_input[0])
            
            if user_input[0] == 'phone':
                user_input = input(
                'Enter name: \n').lower().split() 
                return com_phone(user_input[0])
            
            if user_input[0] == 'delete':
                user_input = input(
                'Enter name: \n').split() 
                name = user_input
                user_input = input(
                'Enter phone: \n').split()    
                return com_delete(name[0], contact_book.Phone(user_input[0]))
            
            if user_input[0] == 'join':
                user_input = input(
                'Enter name: \n').lower().split() 
                name = user_input
                user_input = input(
                'Enter phone: \n').split()    
                return com_join(name[0], contact_book.Phone(user_input[0]))
            
            if user_input[0] == 'add':
                user_input = input(
                'Enter name: \n').split()
                name = user_input
                user_input = input(
                'Enter phone: \n').split()
                phone = user_input
                user_input = input( 
                'Enter email "email@email.com": \n') 
                email = contact_book.Email(
                    user_input) if len(user_input) > 5 else None
                user_input = input( 
                'Enter birthday "YYYY-MM-DD": \n')
                birthday = contact_book.Birthday(
                    user_input) if len(user_input) > 9 else None
                return com_add(contact_book.Name(name[0]), contact_book.Phone(phone[0]), email, birthday)
            
            if user_input[0] == 'change':
                user_input = input(
                'Enter name: \n').split()
                name = user_input
                user_input = input(
                'Enter old phone: \n').split()
                phone = user_input
                user_input = input( 
                'Enter new phone: \n').split()             
                return com_change(name[0], phone[0], contact_book.Phone(user_input[0]))
            
            else:
                continue
    
    if user_input[:2] == ['good', 'bye'] or user_input[0] in ('close', 'exit'):
        return com_exit()
    
    if user_input[0] == 'noter':
        while True:
            user_input = input(
                'Enter your command (scan, add, add tag, find by text, sort by tag, edit, show content by text, show content by tag, delete, show note or exit/close/good bye):\n').lower().split() 
            
            if user_input[:2] == ['good', 'bye'] or user_input[0] in ('close', 'exit'):
                return com_exit()
            
            if user_input[0] == 'scan':
                return Noter.noter.scan()
 
            if user_input[:4] == ['show', 'content','by', 'text']:
                return Noter.noter.show_content_by_text()

            if user_input[:4] == ['show', 'content','by', 'tag']:
                return Noter.noter.show_content_by_tag()

            if user_input[0] == 'add':
                user_input = input(
                'Enter name: \n').split() 
                name = user_input[0]
                user_input = input(
                'Enter text: \n')
                text = user_input
                user_input = input( 
                'Enter tag: \n')
                tag = user_input if len(user_input) != 1 else None
                Noter.noter.add(name,text,tag)
                return "add qqq"
            
            if user_input[0] == 'delete':
                user_input = input(
                'Enter name: \n').split() 
                print(Noter.noter.delete(user_input[0]))
                return "add qqq"                

            if user_input[:2] == ['show', 'note']:
                user_input = input(
                'Enter name: \n').split() 
                print(Noter.noter.show_note(user_input[0]))
                return "add qqq"  

            if user_input[0] == 'edit':
                user_input = input(
                'Enter name: \n').split() 
                name = user_input[0]
                user_input = input(
                'Enter text: \n')
                text = user_input
                user_input = input( 
                'Enter tag: \n')
                tag = user_input if len(user_input) != 1 else None
                print(Noter.noter.edit(name,text,tag))
                return "add qqq"
 
            if user_input[:2] == ['add','tag']:
                user_input = input(
                'Enter name: \n').split() 
                name = user_input[0]
                user_input = input( 
                'Enter tag: \n')
                Noter.noter.add_tag(name,user_input)
                return "add qqq"
                            
            if user_input[:3] == ['find', 'by', 'text']:
                user_input = input(
                'Enter text: \n')
                Noter.noter.find_by_text(user_input)
                return "add qqq"

            if user_input[:3] == ['sort', 'by', 'tag']:
                user_input = input(
                'Enter tag: \n')
                Noter.noter.sort_by_tag(user_input)
                return "add qqq"

            else:
                continue
    
    if user_input[:2]== ['sort', 'file']:
            user_input = input('Enter the directory for sorting (disk:/folder/folder/) ').split()
            sort_file.start(user_input[0])
            return 'start'
    else:
        raise KeyError(user_input[0])


@ input_error


def signal_handler(signal, frame):
    contact_list.save_dumped_data()
    sys.exit(0)


contact_list = contact_book.AddressBook()


if __name__ == '__main__':
    path = pathlib.Path('contact_list.txt')

    if path.exists() and path.stat().st_size > 0:
        contact_list = contact_list.read_dumped_data()
    Noter.Noter.add
    while True:
        user_input = input(
            'Enter your command (contact book, noter, sort file, show all or exit/close/good bye):\n').lower().split()
        result = get_command_handler(user_input)
        if result == 'Good bye!\n':
            print(result)
            break
        if result == 'start':
            print('complite')
        if result == "add qqq":
            print("add qqq")
        elif inspect.isgenerator(result):
            for n in result:
                for rec in n:
                    print(f'name: {rec.name.value}; phone: {", ".join([phone.value for phone in rec.phones])}; '
                          f'email {rec.email.value if rec.email else "-"} ' 
                          f'birthday {rec.birthday.value if rec.birthday else "-"} '
                          f'{"("+str(rec.days_to_birthday())+" days)" if rec.days_to_birthday() else ""}. ')
        else:
            print(result)    
            signal.signal(signal.SIGINT, signal_handler)

    serialized_list = contact_list.save_dumped_data()