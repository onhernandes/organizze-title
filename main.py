from mongoengine import *
from transactions import *
import organizze
import re
import config

config.ensure()

connect('organizze-title-indexer')

def check_old_title(title, notes, category):
    if notes is None:
        return None

    old_title = re.match(r"OLD_TITLE=(.*)", notes)
    old_title = old_title.group().replace("OLD_TITLE=", "") if old_title else False

    t = Transaction.objects(title=old_title).first()

    if old_title is False or t:
        return None

    print("Registering a new item...")
    if category is not None:
        return Transaction(title=old_title, new_title=title, category=category).save()

    return Transaction(title=old_title, new_title=title).save()

def check(id, title, notes, category):
    t = Transaction.objects(title=title).first()

    if t is None:
        return check_old_title(title, notes, category)

    print("Updating transaction")
    new_title = t["new_title"]
    body = { "description": new_title }

    if t["category"] is not None and category is None:
        body["category_id"] = t["category"]

    organizze.update_transaction(id, body)

def main():
    transactions = organizze.list_transactions()

    for t in transactions:
        check(t["id"], t["description"], t["notes"], t["category_id"])

    return "Done!"

if __name__ == "__main__":
    print(main())

