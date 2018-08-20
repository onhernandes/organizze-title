import yaml
import sys
import os

with open("config.yaml", "r") as f:
    y = yaml.load(f)

def get(k):
    return os.environ.get(k, y.get(k))

def ensure():
    values = map(lambda k: get(k), list(y.keys()))

    if not all(list(values)):
        print(
            """
            You must set the Organizze's key either as a envinronment variable or within config.yaml
            - Set $ORGANIZZE_KEY
            """
        )

