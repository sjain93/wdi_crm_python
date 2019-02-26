from contact import Contact


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
            self.modify_existing_contact()
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
        new_contact = Contact.create(new_first_name, new_last_name, new_email, new_note)
        print("New contact added:\n{}".format(new_contact))
  #
  #
  # def modify_existing_contact(self):
  #
  #
  # def delete_contact(self):
  #
  #
  # def display_all_contacts(self):
  #
  # def search_by_attribute(self):


a_crm_app = CRM()
a_crm_app.main_menu()
