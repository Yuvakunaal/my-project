# Mini Project - 1 : Simple Contact book

import os
class Contact:
    def __init__(self,name,phno,email):
        self.name = name
        self.phno = phno
        self.email = email
    def display_details(self):
        return f"Name = {self.name}\nPhone number = {self.phno}\nEmail = {self.email}\n-------------"
class Contact_Book:
    def __init__(self,filename="contact.txt"):
        self.fname = filename
        self.contacts = self.load_contacts()
    def load_contacts(self):
        if not os.path.exists(self.fname):
            return []
        with open(self.fname,"r") as file:
            lines = file.readlines()
        contacts = []
        for line in lines:
            name,phno,email = line.strip().split(",")
            contacts.append(Contact(name,phno,email))
        return contacts
    def save_contacts(self):
        with open(self.fname,"w") as file:
            for contact in self.contacts:
                file.write(f"{contact.name},{contact.phno},{contact.email}\n")
    def add_contacts(self,contact):
        self.contacts.append(contact)
        self.save_contacts()
    def view_contacts(self):
        for contact in self.contacts:
            print("\n"+contact.display_details())
    def delete_contacts(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        print(f"Deleted {name}")
        self.save_contacts()
obj = Contact_Book()
# obj.add_contacts(Contact("kunaal","1234567890","a@b.com"))
# obj.add_contacts(Contact("Hello","0123456789","c@d.com"))

# obj.view_contacts()
# obj.delete_contacts("Hello")
# obj.view_contacts()

# obj.add_contacts(Contact("Unknown","1111111111","aaa@bbb.com"))
obj.view_contacts()
