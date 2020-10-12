"""A company may have sponshorships for events and open positions"""
from peewee import IntegerField, SqliteDatabase, Model, CharField, ForeignKeyField


db = SqliteDatabase('sponsors.sqlite')


class Company(Model):
    name = CharField(unique=True, primary_key=True)
    tagline = CharField(default='')
    website = CharField(default='')
    technologies = CharField(default='')

    class Meta:
        database = db


class OpenPosition(Model):
    company = ForeignKeyField(Company, backref='open_positions')
    title = CharField(null=False)
    url = CharField(null=False)

    class Meta:
        database = db


class Sponsorship(Model):
    company = ForeignKeyField(Company, backref='sponsorships')
    category = IntegerField() 
    event = CharField()

    class Meta:
        database = db


def create_things():
    """Create two companies as sponsors and open positions"""
    with db.connection_context():
        db.create_tables([Company, OpenPosition, Sponsorship])

        onapsis = Company.create(
            name='Onapsis',
            tagline='Protecting Mission-Critical Applications',
            website='https://onapsis.com/',
            technologies='Python,GraphQL,Javascript'
        )
        OpenPosition(
            company=onapsis, title='Sr Python Dev', url='https://onapsis.com/company/careers'
        ).save()    
        OpenPosition(
            company=onapsis, title='Jr Python Dev', url='https://onapsis.com/company/careers'
        ).save()
        Sponsorship(
            company=onapsis, category=1, event='Pyconar 2020'
        ).save()


        morgan = Company.create(
            name='JP Morgan',
            tagline='The right relationship is everything',
            website='https://www.jpmorgan.com/',
            technologies='Python,SciPy,numpy'
        )
        OpenPosition(
            company=morgan, title='Sr Python Dev', url='https://onapsis.com/company/careers'
        ).save()    
        Sponsorship(company=morgan, category=1, event='Pyconar 2020').save()

# Uncomment to create tables
# create_things()