import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    
    intr_dict = dict()

    for i in range(len(transactions["id"])):

        date = transactions["trans_date"][i]
        country = transactions["country"][i]
        state = transactions["state"][i]
        amt = transactions["amount"][i]

        mod_date = str(date)[0 : 7]
        if(pd.isna(country)):
            nan = country

        key = str(mod_date) + "#" + str(country)

        if(key not in intr_dict):
            intr_dict[key] = [0, 0, 0, 0]
        
        intr_dict[key][0] += 1
        intr_dict[key][2] += amt

        if(state == "approved"):
            intr_dict[key][1] += 1
            intr_dict[key][3] += amt

    
    data = []

    for key, vals in intr_dict.items():

        temp = key.split("#")
        month = temp[0]
        country = temp[1]

        if(country == "None"):
            country = nan

        data.append([month, country, vals[0], vals[1], vals[2], vals[3]])

    return pd.DataFrame(data, columns = ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"])


