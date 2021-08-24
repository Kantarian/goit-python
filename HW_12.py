from collections import UserDict
from datetime import *
import json
import os



class AddressBook(UserDict):

    name = ''

    def add_record(self, record):
        self.data[record.name] = {}
        self.data[record.name]['name'] = record.name
        self.data[record.name]['phones'] = record.phones
        self.data[record.name]['emails'] = record.emails
        self.data[record.name]['birthday'] = record.birthday
        self.name = record.name
        return self.name
    
    def iterator(self, start, end):
        info = ''
        for id in self.data:
            if id > start and id < end + 1:
                info = info + '\n' + str(self.data[id])
        return info

    def save_info (self, info):
        if not os.path.isfile(f"{self.name}.json"):
            with open (f"{self.name}.json", 'w') as file:
                json.dump(info, file)

    def update_info (self, new_name = None, new_phone = None, new_email = None, new_birthday = None ):
        if os.path.isfile(f"{self.name}.json"):
            with open (f"{self.name}.json") as file:
                old_data = json.load(file)
                if new_name:
                    old_data[self.name]['name'] = new_name 
                if new_phone:
                    old_data[self.name]['phones'] = new_phone 
                if new_email:
                    old_data[self.name]['emails'] = new_email 
                if new_birthday:
                    old_data[self.name]['birthday'] = new_birthday 
            with open (f"{self.name}.json", 'w') as file:    
                json.dump(old_data, file)
    
    def find_name_phone (self, f_name = None, f_phone = None):
        listdir = os.listdir()
        new_listdir = []
        f_data = ''
        for jsonfile in listdir:
            if jsonfile.find("json") != -1:
                new_listdir.append(jsonfile)
        for jsonfile in new_listdir:   
            with open (jsonfile) as file:
                old_data = json.load(file)
                jname = jsonfile.split('.')
                if f_name or f_phone:
                    for phone in old_data[jname[0]]['phones']:
                        if old_data[jname[0]]['name'].find(f'{f_name}') != -1 or phone.find(f'{f_phone}') != -1:
                            f_data = f_data + '\n' + jname[0]
                
        
        return f_data


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
