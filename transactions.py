from mongoengine import *

class Transaction(Document):
    title = StringField()
    new_title = StringField()

