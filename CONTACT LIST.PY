#CONTACTS LIST PROJECT IN PYTHON
class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number

class ContactsList:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def display_contacts(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            print("Contacts:")
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact.name}: {contact.phone_number}")

def main():
    contacts_list = ContactsList()

    while True:
        print("\n1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter contact's name: ")
            phone_number = input("Enter contact's phone number: ")
            contact = Contact(name, phone_number)
            contacts_list.add_contact(contact)
            print("Contact added successfully!")
        elif choice == '2':
            contacts_list.display_contacts()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
