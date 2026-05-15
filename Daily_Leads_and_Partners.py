import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    lead_id_dict = dict()
    partner_id_dict = dict()


    i = 0
    while(i < len(daily_sales["date_id"])):

        key = (daily_sales["date_id"][i], daily_sales["make_name"][i])

        if(key not in lead_id_dict):
            lead_id_dict[key] = {daily_sales["lead_id"][i]}
            partner_id_dict[key] = {daily_sales["partner_id"][i]}
        
        else:
            lead_id_dict[key].add(daily_sales["lead_id"][i])
            partner_id_dict[key].add(daily_sales["partner_id"][i])

        i += 1
    
    date_id = []
    make_name = []
    unique_lead_id = []
    unique_partner_id = []

    for key, value in lead_id_dict.items():
        date_id.append(key[0])
        make_name.append(key[1])
        unique_lead_id.append(len(value))
        unique_partner_id.append(len(partner_id_dict[key]))


    data = {
        "date_id" : date_id,
        "make_name" : make_name,
        "unique_leads" : unique_lead_id,
        "unique_partners" : unique_partner_id
    }

    return pd.DataFrame(data)