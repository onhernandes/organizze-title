from mongoengine import *

class Category(Document):
    id = IntField(required=True, unique=True)
    parent_id = IntField()
    name = StringField(required=True)

class Transaction(Document):
    title = StringField()
    new_title = StringField()
    category = LazyReferenceField(Category)

