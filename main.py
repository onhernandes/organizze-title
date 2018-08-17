from mongoengine import *
from transactions import *
import organizze
import re
import os

connect('organizze-title-indexer', port=int(os.environ.get("MONGODB_PORT", 27016)), host=os.environ.get("MONGODB_HOST", "127.0.0.1"))

def check_old_title(title, notes, category):
    if notes is None:
        return None

    old_title = re.match(r"OLD_TITLE=(.*)", notes)
    old_title = old_title.group().replace("OLD_TITLE=", "") if old_title else False

    t = Transaction.objects(title=old_title).first()

    if old_title is False or t:
        return None

    print("Registering a new item...")
    return Transaction(title=old_title, new_title=title, category_id=category).save()

def check(id, title, notes, category):
    t = Transaction.objects(title=title).first()

    if t is None:
        return check_old_title(title, notes, category)

    print("Updating transaction \"%s\" to \"%s\"..." % (title, new_title))
    new_title = t["new_title"]
    body = { "description": new_title }

    if t["category_id"] is not None and category is not None:
        body["category_id"] = t["category_id"]

    organizze.update_transaction(id, body)

def category_insert(cat):
    return Category.objects(id=int(cat["id"])).update_one(set__name=cat["name"], set__parent_id=cat["parent_id"], upsert=True)

def main():
    categories = organizze.list_categories()
    map(category_insert, categories)

    transactions = organizze.list_transactions()

    for t in transactions:
        check(t["id"], t["description"], t["notes"], t["category_id"])

    return "Done!"

if __name__ == "__main__":
    print(main())

