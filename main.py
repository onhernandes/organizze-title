from mongoengine import *
from transactions import Transaction
import organizze
import re

connect('organizze-title-indexer', port=27016)

def check_old_title(title, notes):
    old_title = re.search(r"OLD_TITLE=(.*)", notes)
    old_title = old_title.group() if old_title else False

    if not old_title:
        return None

    return Transaction(title=old_title, new_title=title).save()

def check(id, title, notes):
    if notes is not None and "OLD_TITLE=" in notes:
        return check_old_title(title, notes)

    t = Transaction.objects(title=title).first()

    if not t:
        return None

    new_title = t[0].new_title
    return organizze.update_transaction(id, { "title": new_title })

def main():
    transactions = organizze.list_transactions()

    for t in transactions:
        check(t["id"], t["description"], t["notes"])

if __name__ == "__main__":
    print(main())

