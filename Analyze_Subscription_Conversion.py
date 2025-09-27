import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    
    free = dict()
    paid = dict()

    for i in range(len(user_activity["user_id"])):

        user_id = user_activity["user_id"][i]
        activity_type = user_activity["activity_type"][i]
        activity_duration = user_activity["activity_duration"][i]

        if(activity_type == "free_trial"):

            if(user_id not in free):
                free[user_id] = [activity_duration]
            else:
                free[user_id].append(activity_duration)
        
        elif(activity_type == "paid"):

            if(user_id not in paid):
                paid[user_id] = [activity_duration]
            else:
                paid[user_id].append(activity_duration)
    

    user_id = []
    trial_avg_duration = []
    paid_avg_duration = []

    for id, duration in free.items():

        if(id in paid):
            paid_duration = paid[id]
            user_id.append(id)
            trial_avg_duration.append(round(sum(duration)/len(duration) + 1e-9, 2))
            paid_avg_duration.append(round(sum(paid_duration)/len(paid_duration) + 1e-9, 2))
    
    data = {
        "user_id" : user_id,
        "trial_avg_duration" : trial_avg_duration,
        "paid_avg_duration" : paid_avg_duration
    }

    return pd.DataFrame(data)