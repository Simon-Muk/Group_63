class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone = phone_number

    @classmethod
    def validate_phone_number(cls, phone_number):
        # Проверяем что номер состоит из 10 цифр
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        return False


class ContactList:
    all_contacts = []

    @classmethod
    def add_contact(cls, name, phone_number):
        # 1. Проверяем номер
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)

            cls.all_contacts.append(new_contact)
        else:
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")
print(ContactList.all_contacts)  # []

ContactList.add_contact("Вася Пупкин", "0700100200")
ContactList.add_contact("Виктор Цой", "0500123456")

for contact in ContactList.all_contacts:
    print(contact.name, contact.phone)
