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
- Get a token from Organizze [https://app.organizze.com.br/configuracoes/api-keys](https://app.organizze.com.br/configuracoes/api-keys)
- Use with: `USERNAME=<your organizze's username> TOKEN=<the token u got> USER_AGENT=<your name(email)> python main.py`

