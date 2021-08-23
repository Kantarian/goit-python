from collections import UserDict
from datetime import *

class AddressBook(UserDict):
    id = 0

    def add_record(self, record):
        self.data[self.id] = {}
        self.data[self.id]['name'] = record.name
        self.data[self.id]['phones'] = record.phones
        self.data[self.id]['emails'] = record.emails
        self.data[self.id]['birthday'] = record.birthday
        self.id += 1 
        return self.id
    
    def iterator(self, start, end):
        info = ''
        for id in self.data:
            if id > start and id < end + 1:
                info = info + '\n' + str(self.data[id])
        return info

class Record():
    phones = []
    emails = []
    names = []
    __birthday = []

    def __init__(self, name):
        self.name = name
        self.names.append(name)

    def add_contacts(self, phone = None, email = None, birthday = None):

        if phone:
            self.__phone = None
            self.phone = phone
            self.phones.append(self.__phone)
        if email:
            self.emails.append(email)
        if birthday:
            self.__birthday = None
            self.birthday = birthday
        
    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if (type(birthday) == list) and (len(birthday) == 3) and (type(birthday[0]) == int):
            self.__birthday = birthday
        else:
            print('not list')
    
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if (type(phone) == str) and (phone[0:4] == '+380'):
            self.__phone = phone

    def remove_contacts(self, phone = None, email = None):
        if phone:
            self.phones.remove(phone)
        if email:    
            self.emails.remove(email)

    def change_contacts(self, old_value = None, new_phone = None, new_email = None):
        for phon in self.phones:
            count = 0
            if phon != old_value:
                count = count+1
            else:
                self.phones[count] = new_phone    

        for phon in self.emails:
            count = 0
            if phon != old_value:
                count = count+1
            else:
                self.emails[count] = new_email        

    def days_to_birthday(self):
        now_ywd = datetime.now().timetuple()
        now_date = date(now_ywd[0], now_ywd[1], now_ywd[2])
        self.birthday[0] = now_ywd[0]
        days_to_birthday = date(self.birthday[0], self.birthday[1], self.birthday[2])
        delta = (days_to_birthday - now_date).days
        if delta < 0:
            self.birthday[0] = now_ywd[0] + 1
            days_to_birthday = date(self.birthday[0], self.birthday[1], self.birthday[2])
            delta = (days_to_birthday - now_date).days
            return f'Days left {delta}'
        if delta == 0:
            return f'Today is birthday of {self.name}'
        else:
            return f'Days left {delta}'      



class Field():
    pass

class Name(Field):
    name = ''
    def __init__(self, name):
        self.__name = None
        self.name = name

class Phone(Field):
    def add_phone (self, phone):
        self.__phone = None
        self.phone = phone

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        if (type(phone) == str) and (phone[0:4] == '+380'):
            self.__phone = phone

class Birthday(Field):
    def add_birthday (self, birthday):
        self.__birthday = None
        self.birthday = birthday
    
    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, birthday):
        if (type(birthday) == list) and (len(birthday) == 3) and (type(birthday[0]) == int):
            self.__birthday = birthday
        else:
            print('not list')


