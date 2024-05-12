from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
        def __init__(self,value):
            super().__init__(value)
            assert len(str(self.value)) == 10
        'Number is too short'

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        self.phones = [i for i in self.phones if i.value != phone]

    def edit_phone(self,new, old):
        for i in self.phones:
            if i.value == old:
                i.value = new


    def find_phone(self,phone):
        return [i for i in self.phones if i.value == phone]


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value] = record
    def find(self,name):
        return self.data.get(name)

    def delete(self,name):
        return self.data.pop(name)




