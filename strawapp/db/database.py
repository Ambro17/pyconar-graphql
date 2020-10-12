from peewee import SqliteDatabase, Model, CharField


db = SqliteDatabase('sponsors.db')


class Sponsor(Model):
    name = CharField()

    class Meta:
        database = db