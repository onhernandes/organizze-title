from mongoengine import *
from transactions import Transaction
import organizze
import re

def check(id, title, notes):
    if "OLD=" in notes:
        pass

    t = Transaction.objects(title=title)

    if not len(t):
        return Transaction(title=title, organizze_id=id, new_title=title).save()

    organizze.update_transaction(id, { "title": title })

def main():
    transactions = organizze.list_transactions()

    for t in transactions:
        check(t["id"], t["description"])

if __name__ == "__main__":
    main()
