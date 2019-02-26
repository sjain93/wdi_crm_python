from peewee import SqliteDatabase, Model, CharField, TextField

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


db.connect()
db.create_tables([Contact])
