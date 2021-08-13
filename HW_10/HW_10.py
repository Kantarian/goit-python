from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data['name'] = record.name
        self.data['phones'] = record.phones
        self.data['emails'] = record.emails



class Record(AddressBook):
    phones = []
    emails = []
    names = []

    def __init__(self, name):
        self.name = name
        self.names.append(name)

    def add_contacts(self, phone = None, email = None):
        if phone:
            self.phones.append(phone)
        if email:
            self.emails.append(email)

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

class Field():
    pass

class Name():
    name = ''
    def __init__(self, name):
        self.name = name

class Phone():
    def add_phone (self, phone):
        self.phone = phone
