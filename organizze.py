import requests
import os

API_BASE_URL = "https://api.organizze.com.br/rest/v2"
headers = { \
    "user-agent": os.environ.get("USER_AGENT", "")
}

# https://app.organizze.com.br/configuracoes/api-keys
auth = (os.environ.get("USERNAME"), os.environ.get("TOKEN")) 

def list_transactions():
    """
    List Organizze's transactions

    """
    r = requests.get(f"{API_BASE_URL}/transactions", headers=headers, auth=auth)
    return r.json()

def update_transaction(id, body):
    """
    Update a transaction
    """
    r = requests.put(f"{API_BASE_URL}/transactions/{id}", data=body, headers=headers, auth=auth)
    return r.json()

