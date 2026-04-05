import pandas as pd

def sum_daily_odd_even(transactions: pd.DataFrame) -> pd.DataFrame:
    
    trans_dict = {}

    for i in range(len(transactions["transaction_id"])):

        tras_date = transactions["transaction_date"][i]
        amt = transactions["amount"][i]

        if(tras_date not in trans_dict):
            trans_dict[tras_date] = [0, 0]
        
        if(amt % 2 == 0):
            trans_dict[tras_date][1] += amt
        else:
            trans_dict[tras_date][0] += amt

    trans_date = []
    odd_sum = []
    even_sum = []

    data = []

    for date, amts in trans_dict.items():
        data.append([date, amts[0], amts[1]])
    
    data.sort()

    return pd.DataFrame(data, columns=["transaction_date", "odd_sum", "even_sum"])