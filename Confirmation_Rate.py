import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    
    d = dict()

    for i in range(len(confirmations["user_id"])):

        user_id = confirmations["user_id"][i]
        action = confirmations["action"][i]

        if(user_id not in d):
            d[user_id] = [0, 0]

        if(action == "confirmed"):
            d[user_id][0] += 1
        
        d[user_id][1] += 1

    
    u_id = []
    c_rate = []

    for i in range(len(signups)):
        user_id = signups["user_id"][i]

        u_id.append(user_id)

        if(user_id in d):
            c_rate.append(round(d[user_id][0]/d[user_id][1], 2))
        else:
            c_rate.append(0)
    
    data = {
        "user_id" : u_id,
        "confirmation_rate" : c_rate
    }

    return pd.DataFrame(data)