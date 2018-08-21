# organizze-title

Title matching for my Organizze's transactions

It looks for Organizze's transactions, and do some tricks:

- If there is `OLD_TITLE=` into `notes`, then gets the data and inserts into a MongoDB Collection
- If not, look for the title into MongoDB's collection, gets the new title and update on Organizze

It is useful if you have to transcript wrong and mispelled names from bank account's notifications and SMS to Organizze using the SMS/notifications import feature.

## Usage

- Clone this repo: `git clone git@github.com:onhernandes/organizze-title.git`
- `cd organizze-title`
- Create a virtualenv(optional but recommended): `mkdir env && virtualenv --python=$(which python3) env && source env/bin/activate`
- Install packages: `pip install -r requirements.txt`
- Set the keys
  - You can use environment variables or set them within `config.yaml`
  - Keys:
    - `ORGANIZZE_USERNAME`: your Organizze's username
    - `ORGANIZZE_KEY`: your Organizze's token, acquired [here](https://app.organizze.com.br/configuracoes/api-keys)
    - `ORGANIZZE_USER_AGENT`: your name (your website/email) like `Matheus(https://hernandes.io)`

--------

License MIT
