'''

@Author:  joshikarsn

@Date: 2024-01-27 11:25:30

@Last Modified by:  joshikarsn

@Last Modified time: 2024-01-27 11:25:30

@Title : AddressBook Problem
'''
import json

class Contact:
   def __init__(self, fname, lname, address, city, state, zip_code, phno, email):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip_code
        self.phno = phno
        self.email = email

   def __repr__(self) -> str:
      return f'{self.fname}'

class AddressBook:
   def __init__(self, name):
        self.book_name = name
        self.contacts = {}

   def add_contact(self, contact):
        if contact.fname not in self.contacts:
          self.contacts[contact.fname] = contact
        else:
            print("The Contact already exists")

   def add_contacts(self):
       while True:
            option = int(input("Enter 1 to add a new contact, 2 to break: "))
            if option == 1:
                fname = input("Enter the person's fname: ")
                lname = input("Enter the person's lname: ")
                address = input("Enter the person's address: ")
                city = input("Enter the person's city: ")
                state = input("Enter the person's state: ")
                zip_code = input("Enter the person's zip: ")
                phno = input("Enter the person's phno: ")
                email = input("Enter the person's email: ")
                contact = Contact(fname, lname, address, city, state, zip_code, phno, email)
                self.add_contact(contact)
            else:
               break

   def delete_contact(self, fname):
        if fname in self.contacts:
            self.contacts.pop(fname)
        else:
            print("The Contact doesn't exist")

   def get_contact(self, fname):
       if fname in self.contacts:
          contact = self.contacts[fname]
          print(f''' 
                     fname:{contact.fname}
                     lname:{contact.lname}
                     address:{contact.address}
                     city:{contact.city}
                     state:{contact.state}
                     zip:{contact.zip}
                     phno:{contact.phno}
                     email:{contact.email}
               ''')
       else:
          print("The Person doesn't exist")

   def edit_contact(self, fname):
        if fname in self.contacts:
            contact = self.contacts[fname]
            while True:
                edit = int(input("Enter 1 to change address, 2 to change city, 3 to change zip, 4 to change phno, 5 to change email: "))
                if edit == 1:
                  new_address = input("Enter the new address: ")
                  contact.address = new_address
                elif edit == 2:
                  new_city = input("Enter the new city: ")
                  contact.city = new_city
                elif edit == 3:
                  new_zip = input("Enter the new zip: ")
                  contact.zip = new_zip
                elif edit == 4:
                  new_phno = input("Enter the new phno: ")
                  contact.phno = new_phno
                elif edit == 5:
                  new_email = input("Enter the new email: ")
                  contact.email = new_email
                else:
                   break
        else:
           print("The contact doesn't exist ")

   def contact_by_city_or_state(self, city_or_state):
      contacts = list(filter(lambda contact: city_or_state in [contact.city, contact.state], self.contacts.values()))
      print(contacts)

class MultiAddressBook:
   def __init__(self):
       self.books_dict = {}
       self.json_file = 'address_book.json'

   def get_book(self, book_name):
       return self.books_dict.get(book_name)

   def add_addressbook(self, addressbook):
        if addressbook.book_name in self.books_dict:
          print("The Address Book already exists")
        else:
          self.books_dict[addressbook.book_name] = addressbook

   def delete_addressbook(self, name):
       if name in self.books_dict:
          del self.books_dict[name]

   def get_contacts_by_city_or_state(self, city_or_state):
      list(map(lambda book: book.contact_by_city_or_state(city_or_state), self.books_dict.values()))

   def save_to_json(self):
      json_data = {}
      with open(self.json_file, 'w') as file:
         for name, book_obj in self.books_dict.items():
            if not name in json_data:
               json_data[name] = {}
            contact_data = json_data.get(name)
            for contact_obj in book_obj.contacts.values():
               contact_data.update({contact_obj.fname: contact_obj.__dict__})
         json.dump(json_data, file, indent=4)
         print(json.dumps(json_data), type(json.dumps(json_data)))

def get_book_obj(books):
   book_name = input('Enter book name: ')
   book = books.get_book(book_name)
   if not book:
      book = AddressBook(book_name)
   return book

if __name__ == "__main__":
   books =  MultiAddressBook()
   while True:
        choice = int(input("Enter 1 for add contacts, 2 for edit contact,3 for get contacts,4 for get contacts by cityorstate,5 for delete contacts, 6 to exit: "))
        if choice == 1:
            book = get_book_obj(books)
            books.add_addressbook(book)
            book.add_contacts()
            books.save_to_json()
        elif choice == 2:
           book = get_book_obj(books)
           name = input("Enter the name of the Person: ")
           book.edit_contact(name)
        elif choice == 3:
           book = get_book_obj(books)
           name = input("Enter the name of the Person: ")
           book.get_contact(name)
        elif choice == 4:
           city_or_state = input("Enter the city or state: ")
           books.get_contacts_by_city_or_state(city_or_state)
        elif choice == 5:
           book = get_book_obj(books)
           name = input("Enter the name of the Person: ")
           book.delete_contact(name)
        elif choice == 6:
           break