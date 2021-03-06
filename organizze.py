import requests
import config

API_BASE_URL = "https://api.organizze.com.br/rest/v2"
headers = { \
    "user-agent": config.get("ORGANIZZE_USER_AGENT")
}

# https://app.organizze.com.br/configuracoes/api-keys
auth = (config.get("ORGANIZZE_USERNAME"), config.get("ORGANIZZE_KEY")) 

def list_transactions():
    """
    List Organizze's transactions

    """
    r = requests.get("%s/transactions" % (API_BASE_URL), headers=headers, auth=auth)
    return r.json()

def update_transaction(id, body):
    """
    Update a transaction
    """
    r = requests.put("%s/transactions/%s" % (API_BASE_URL, id), data=body, headers=headers, auth=auth)
    return r.json()

def list_categories():
    """
    List Organizze's categories

    """
    r = requests.get("%s/categories" % (API_BASE_URL), headers=headers, auth=auth)
    return r.json()

