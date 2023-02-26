from collections import UserDict


class Field:
    # батьківський для всіх полів, потім в ньому реалізуємо логіку
    pass


class Name(Field):
    def __init__(self, name):
        self.value = name


class Phone(Field):
    # необов'язкове поле з телефоном та таких один запис (Record) може містити кілька
    def __init__(self, phone):
        self.value = phone


class AddressBook(UserDict):
    # потім додамо логіку пошук за записами до цього класу
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    # відповідає за логіку додавання/видалення/редагування необов'язкових полів,
    # та зьерігання обов'язкогового поля name
    def __init__(self, name, new_phone):
        self.name = name
        self.phones = []
        if new_phone:
            self.add_phone(new_phone)

    def add_phone(self, new_phone):
        self.phones.append(new_phone)

    def change_phone(self, old_phone, new_phone):
        for ph in self.phones:
            if ph.value == old_phone:
                self.phones.add_phone(new_phone)
                self.phones.remove_phone(ph)
            else:
                print(f'This phone - {old_phone} is not in list')

    def remove_phone(self, old_phone):
        for ph in self.phones:
            if ph.value == old_phone:
                self.phones.remove(ph)
            else:
                print(f"This phone {old_phone} is exist in list")


if __name__ == '__main__':
    name = Name('Sem')
    phone = Phone('111')
    rec = Record(name, phone)
    address_book = AddressBook()
    address_book.add_record(rec)
