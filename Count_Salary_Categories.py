import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    low = 0
    avg = 0
    high = 0

    for i in range(len(accounts["account_id"])):
        income = accounts["income"][i]

        if(income < 20000):
            low += 1
        elif(income > 50000):
            high += 1
        else:
            avg += 1

        i += 1
    
    data = {
        "category" : ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count" : [low, avg, high]
    }

    return pd.DataFrame(data)