class ContactsManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone_number, email_address):
        if name not in self.contacts:
            self.contacts[name] = {'phone_number': phone_number, 'email_address': email_address, 'views': 0}
            print(f"Contact '{name}' added successfully.")
        else:
            print(f"Contact '{name}' already exists.")

    def update_contact(self, name, phone_number=None, email_address=None):
        if name in self.contacts:
            if phone_number:
                self.contacts[name]['phone_number'] = phone_number
            if email_address:
                self.contacts[name]['email_address'] = email_address
            print(f"Contact '{name}' updated successfully.")
        else:
            print(f"Contact '{name}' does not exist.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' does not exist.")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"Name: {name}")
            print(f"Phone Number: {self.contacts[name]['phone_number']}")
            print(f"Email Address: {self.contacts[name]['email_address']}")
            print(f"Views: {self.contacts[name]['views']}")
            self.contacts[name]['views'] += 1
        else:
            print(f"Contact '{name}' not found.")

    def display_all_contacts(self):
        print("All Contacts:")
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {info['phone_number']}")
            print(f"Email Address: {info['email_address']}")
            print(f"Views: {info['views']}")
            print("--------------------")


def main():
    contacts_manager = ContactsManager()

    while True:
        print("\nChoose an option:")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email_address = input("Enter email address: ")
            contacts_manager.add_contact(name, phone_number, email_address)
        elif choice == '2':
            name = input("Enter name of contact to update: ")
            phone_number = input("Enter new phone number (leave empty to skip): ")
            email_address = input("Enter new email address (leave empty to skip): ")
            contacts_manager.update_contact(name, phone_number, email_address)
        elif choice == '3':
            name = input("Enter name of contact to delete: ")
            contacts_manager.delete_contact(name)
        elif choice == '4':
            name = input("Enter name of contact to search: ")
            contacts_manager.search_contact(name)
        elif choice == '5':
            contacts_manager.display_all_contacts()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
