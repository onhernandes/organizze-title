import yaml
import sys
import os

current_dir = os.path.dirname(os.path.realpath(__file__))

def get(k):
    with open(os.path.join(current_dir, "config.yaml"), "r") as f:
        y = yaml.load(f)

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

