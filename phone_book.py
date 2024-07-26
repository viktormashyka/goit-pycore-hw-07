from collections import UserDict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    # реалізація класу
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
              raise ValueError("Phone number must be a string of 10 digits.")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        try:
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
            datetime_object = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(datetime_object)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
        return f"Birthday {birthday} added."

    def __str__(self):
        birthday_str = self.birthday.value.strftime("%d.%m.%Y") if self.birthday else "N/A"
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}, birthday: {self.birthday}"

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
    
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []
        today = datetime.now().date()

        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)
                days_until_birthday = (birthday_this_year - today).days
                if 0 <= days_until_birthday < 7:
                    upcoming_birthdays.append({"name": record.name.value, "congratulation_date": birthday_this_year.strftime("%d.%m.%Y")})
        return upcoming_birthdays


if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("30.07.2006")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("14.05.2011")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Виведення днів народжень на найближчий тиждень
    upcoming_birthdays = book.get_upcoming_birthdays()
    print(upcoming_birthdays) 

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
