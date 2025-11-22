import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:

    user_dict = {}

    for i in range(len(users["account"])):
        user_dict[users["account"][i]] = users["name"][i]
    
    bal_dict = dict()

    for i in range(len(transactions["trans_id"])):

        acc = transactions["account"][i]
        amt = transactions["amount"][i]

        if(acc not in bal_dict):
            bal_dict[acc] = amt
        else:
            bal_dict[acc] += amt

    
    name = []
    balance = []

    for acc, amt in bal_dict.items():

        if(amt > 10000):
            name.append(user_dict[acc])
            balance.append(amt)

    data = {
        "name" : name,
        "balance" : balance
    }

    return pd.DataFrame(data)

