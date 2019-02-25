class Contact:

    contacts = []
    next_id = 1

    def __init__(self, first_name, last_name, email, note):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.note = note
        self.id = Contact.next_id
        Contact.next_id += 1

    @classmethod
    def create(cls, first_name, last_name, email, note):
        valid = next((contact for contact in cls.contacts if contact.email == email), None)
        if valid:
            print("Email address already exists")
        else:
            new_contact = Contact(first_name, last_name, email, note)
            cls.contacts.append(new_contact)
        return new_contact

    @classmethod
    def all(cls):
        for contact in Contact.contacts:
            print("{} {}, {}".format(contact.first_name, contact.last_name, contact.email))

    @classmethod
    def find(cls, ident):
        for contact in cls.contacts:
            if ident == contact.id:
                return "{} {}, {}".format(contact.first_name, contact.last_name, contact.email)

    def update(self):
        """ This method should allow you to specify, chosen instance will come from CRM class
        1. which of the contact's attributes you want to update
        2. the new value for that attribute
        and then make the appropriate change to the contact
        """
        print("Copy and paste the attribute would you like to change:\nfirst_name\nlast_name\nemail\nnote")
        attribute = input()
        validation = ["first_name", "last_name", "email", "note"]
        if attribute in validation:
            print("Ok, what is the new {}?".format(attribute))
            new_attr = input()
            setattr(self, attribute, new_attr)
            print("Attribute updated")
        else:
            print("Invalid attribute provided")

    @classmethod
    def find_by(cls):
        """This method should work similarly to the find method above
        but it should allow you to search for a contact using attributes other than id
        by specifying both the name of the attribute and the value eg.
        searching for 'first_name', 'Betty' should return the first contact named Betty
        """
        print("Please specify an attribute to provide a search")
    pass

    @classmethod
    def delete_all(cls):
        cls.contacts = []

    def full_name(self):
        """Returns the full (first and last) name of the contact"""
        if self in Contact.contacts:
            print("{} {}".format(self.first_name, self.last_name))

    def delete(self):
        """This method should delete the contact
        HINT: Check the Array class docs for built-in methods that might be useful here
        """
        pass


test1 = Contact.create("Sanchit", "Jain", "sanchit.jain@mail.mcgill.ca", "hello")
test2 = Contact.create("Tarishi", "Jain", "smartaru1997@gmail.com", "hello")
test3 = Contact.create("Josh", "Teneycke", "james.mcgill@mail.mcgill.ca", "hello")
print(len(Contact.contacts))
test1.full_name()
test1.update()
Contact.all()
# Contact.delete_all()
print(len(Contact.contacts))
