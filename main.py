from mongoengine import *
from transactions import Transaction
import organizze
import re
import os

connect('organizze-title-indexer', port=int(os.environ.get("MONGODB_PORT", 27016)), host=os.environ.get("MONGODB_HOST", "127.0.0.1"))

def check_old_title(title, notes):
    if notes is None:
        return None

    old_title = re.match(r"OLD_TITLE=(.*)", notes)
    old_title = old_title.group().replace("OLD_TITLE=", "") if old_title else False

    t = Transaction.objects(title=old_title).first()

    if old_title is False or t:
        return None

    print("Registering a new item...\n")
    return Transaction(title=old_title, new_title=title).save()

def check(id, title, notes):
    t = Transaction.objects(title=title).first()

    if t is None:
        return check_old_title(title, notes)

    new_title = t["new_title"]
    print("Updating transaction \"%s\" to \"%s\"...\n" % (title, new_title))
    res = organizze.update_transaction(id, { "description": new_title })
    print(res)
    return res

def main():
    transactions = organizze.list_transactions()

    for t in transactions:
        check(t["id"], t["description"], t["notes"])

if __name__ == "__main__":
    print(main())

