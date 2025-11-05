import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:

    occr_dict = dict()

    for i in range(len(request_accepted["requester_id"])):

        r_id = request_accepted["requester_id"][i]
        a_id = request_accepted["accepter_id"][i]

        if(r_id not in occr_dict):
            occr_dict[r_id] = 1
        else:
            occr_dict[r_id] += 1
        
        if(a_id not in occr_dict):
            occr_dict[a_id] = 1
        else:
            occr_dict[a_id] += 1
    

    max_connection = max(occr_dict.values())

    for key, val in occr_dict.items():

        if(val == max_connection):
            id = key
            break

    data = {
        "id" : [id],
        "num" : [max_connection]
    }

    return pd.DataFrame(data)