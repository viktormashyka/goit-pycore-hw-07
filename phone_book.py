from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, name):
        super().__init__(name)
        # self.value = name

class Phone(Field):
    # реалізація класу
    def __init__(self, phone):
        if len(phone) != 10 or not phone.isdigit():
              raise ValueError("Phone number must be a string of 10 digits.")
        super().__init__(phone)
        # self.phone = phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def add_phone(self, phone):
        new_phone = Phone(phone)
        self.phones.append(new_phone)
        return f"Phone {phone} added."

    def remove_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(phone)
                return f"Phone {phone} removed."
        return f"Phone {phone} not found."

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = new_phone
                return f"Phone {old_phone} updated to {new_phone}."
        return f"Phone {old_phone} not found."
    
    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return f"Phone {phone} not found." 

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, f"Contact {name} not found.")
    
    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return f"Contact {name} deleted."
        return f"Contact {name} not found."


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
