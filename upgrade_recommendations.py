# Functions that recommend upgrades for the BMW 330i xDrive Sedan in the categories engine, suspension and exhaust, based on the user's budget.


# Function to recommend engine upgrade based on user's budget


def recommend_engine_upgrade(budget):
    if budget <= 500:
        return 'engine air filter'
    elif budget <= 1000:
        return 'cold air intake'
    else:
        return 'performance chip tuning'


# Function to recommend suspension upgrade based on user's budget

def recommend_suspension_upgrade(budget):
    if budget <= 1000:
        return 'shock absorbers'
    elif budget <= 3000:
        return 'coilovers'
    else:
        return 'air suspension kit'


# Function to recommend exhaust upgrade based on user's budget

def recommend_exhaust_upgrade(budget):
    if budget <= 1000:
        return 'cat-back exhaust'
    elif budget <= 3000:
        return 'header and cat'
    else:
        return 'turbo-back exhaust'
