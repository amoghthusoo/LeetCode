import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    unique_id_dict = dict()

    for i in range(len(employee_uni["id"])):
        unique_id_dict[employee_uni["id"][i]] = employee_uni["unique_id"][i]
    
    unique_id = []
    name = []

    for i in range(len(employees["id"])):

        if(employees["id"][i] in unique_id_dict):
            unique_id.append(unique_id_dict[employees["id"][i]])
        else:
            unique_id.append(None)
        
        name.append(employees["name"][i])

    data = {
        "unique_id" : unique_id,
        "name" : name
    }

    return pd.DataFrame(data)
