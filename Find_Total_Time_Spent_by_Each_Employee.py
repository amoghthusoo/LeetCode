import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
    intr_dict = {}

    i = 0
    while(i < len(employees)):

        id = employees.loc[i, "emp_id"]
        day = employees.loc[i, "event_day"]
        _in = employees.loc[i, "in_time"]
        out = employees.loc[i, "out_time"]
        
        key = f"{id} {day}"

        if(key not in intr_dict):
            intr_dict[key] = (out - _in)
        else:
            intr_dict[key] += (out - _in)

        i += 1

    day = []
    emp_id = []
    total_time = []

    for key, val in intr_dict.items():
        temp = key.split()
        emp_id.append(int(temp[0]))
        day.append(temp[1])
        total_time.append(val)

    data = {
        "day" : day,
        "emp_id" : emp_id,
        "total_time" : total_time
    }

    return pd.DataFrame(data)