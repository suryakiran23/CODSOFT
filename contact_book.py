class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        results = [contact for contact in self.contacts if query.lower() in contact.name.lower() or query in contact.phone]
        return results

    def update_contact(self, old_contact, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact == old_contact:
                self.contacts[idx] = new_contact
                return True
        return False

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully!")

        elif choice == '2':
            print("Contact List:")
            contact_book.view_contacts()

        elif choice == '3':
            query = input("Enter name or phone to search: ")
            results = contact_book.search_contact(query)
            if results:
                print("Search Results:")
                for contact in results:
                    print(contact)
            else:
                print("No contacts found.")

        elif choice == '4':
            query = input("Enter name or phone of the contact to update: ")
            results = contact_book.search_contact(query)
            if results:
                print("Select a contact to update:")
                for idx, contact in enumerate(results):
                    print(f"{idx + 1}. {contact}")
                selection = int(input("Enter the number of the contact to update: ")) - 1
                old_contact = results[selection]
                name = input("Enter new name: ")
                phone = input("Enter new phone: ")
                email = input("Enter new email: ")
                address = input("Enter new address: ")
                new_contact = Contact(name, phone, email, address)
                contact_book.update_contact(old_contact, new_contact)
                print("Contact updated successfully!")
            else:
                print("No contacts found.")

        elif choice == '5':
            query = input("Enter name or phone of the contact to delete: ")
            results = contact_book.search_contact(query)
            if results:
                print("Select a contact to delete:")
                for idx, contact in enumerate(results):
                    print(f"{idx + 1}. {contact}")
                selection = int(input("Enter the number of the contact to delete: ")) - 1
                contact_to_delete = results[selection]
                contact_book.delete_contact(contact_to_delete)
                print("Contact deleted successfully!")
            else:
                print("No contacts found.")

        elif choice == '6':
            print("Exiting the Contact Book.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
