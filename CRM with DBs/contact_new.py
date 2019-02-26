from peewee import SqliteDatabase, Model

db = SqliteDatabase('crm.db')


class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    email = CharField()
    note = TextField()

    class Meta:
        database = db

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    # def __str__(self):
    #     return "Name: {} {}, email: {}, note: {}".format(self.first_name, self.last_name, self.email, self.note)


db.connect()
db.create_tables([Contact])
# test1 = Contact.create("Sanchit", "Jain", "sanchit.jain@mail.mcgill.ca", "hello")
# test2 = Contact.create("Tarishi", "Jain", "smartaru1997@gmail.com", "hello")
# test3 = Contact.create("Josh", "Teneycke", "james.mcgill@mail.mcgill.ca", "hello")
# print(len(Contact.contacts))
# test1.full_name()
# test1.update()
# Contact.all()
# # Contact.delete_all()
# print(len(Contact.contacts))
