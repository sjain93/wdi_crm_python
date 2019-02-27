from contact_new import Contact


class CRM:

    def main_menu(self):
        while True:   # repeat indefinitely
            self.print_main_menu()
            user_selected = int(input())
            self.call_option(user_selected)

    def print_main_menu(self):
        print('[1] Add a new contact')
        print('[2] Modify an existing contact')
        print('[3] Delete a contact')
        print('[4] Display all the contacts')
        print('[5] Search by attribute')
        print('[6] Exit')
        print('Enter a number: ')

    def call_option(self, user_selected):
        if user_selected == 1:
            self.add_new_contact()
        elif user_selected == 2:
            self.modify_existing_contact()
        elif user_selected == 3:
            self.delete_contact()
        elif user_selected == 4:
            self.display_all_contacts()
        elif user_selected == 5:
            self.search_by_attribute()
        elif user_selected == 6:
            quit()

    def add_new_contact(self):
        print("What is the first name?")
        new_first_name = input()
        print("What is the last name?")
        new_last_name = input()
        print("What is the email?")
        new_email = input()
        print("What is the note?")
        new_note = input()
        new_contact = Contact.create(
            first_name=new_first_name,
            last_name=new_last_name,
            email=new_email,
            note=new_note)
        print("New contact added:\n{}".format(new_contact))

    def modify_existing_contact(self):
        print("Please select the id of the contact you would like to modify")
        for contact in Contact.select():
            print("{} {} {}".format(contact.id, contact.first_name, contact.email))
        input_id = int(input())
        contact_detail = Contact.get(id=input_id)
        # Contact.update(contact_detail)
        print("Copy and paste the attribute would you like to modify:\nfirst_name\nlast_name\nemail\nnote")
        mod_field = input()
        print("What would you like to change {} to?".format(mod_field))
        new_val = input()
        if mod_field == "first_name":
            contact_detail.first_name = new_val
            contact_detail.save()
        elif mod_field == "last_name":
            contact_detail.last_name = new_val
            contact_detail.save()
        elif mod_field == "email":
            contact_detail.email = new_val
            contact_detail.save()
        elif mod_field == "note":
            contact_detail.note = new_val
            contact_detail.save()
        print("Contact updated")

    def delete_contact(self):
        print("Please select the id of the contact you would like to delete")
        for contact in Contact.select():
            print("{} {} {}".format(contact.id, contact.first_name, contact.email))
        input_id = int(input())
        contact_detail = Contact.get(id=input_id)
        contact_detail.delete_instance()
        print("contact deleted")

    def display_all_contacts(self):
        for contact in Contact.select():
            print("{} {} {} {}".format(contact.id, contact.first_name, contact.email, contact.note))

    def search_by_attribute(self):
        print("Copy and paste the attribute would you like to search by:\nfirst_name\nlast_name\nemail\nnote")
        search_field = input()
        print("What value would you like to search by?")
        search_value = input()
        if search_field == "first_name":
            result = Contact.get(Contact.first_name == search_value)
        elif search_field == "last_name":
            result = Contact.get(Contact.last_name == search_value)
        elif search_field == "email":
            result = Contact.get(Contact.email == search_value)
        elif search_field == "note":
            result = Contact.get(Contact.note == search_value)
        else:
            print("Incorrect query")
        if result:
            print("Your contact:{} {}, email: {}, note {}".format(result.first_name, result.last_name, result.email, result.note))
        else:
            print("Incorrect query")

a_crm_app = CRM()
a_crm_app.main_menu()
