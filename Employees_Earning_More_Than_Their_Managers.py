import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:

    data_dict = {}

    for i in range(len(employee["id"])):

        id = employee["id"][i]
        name = employee["name"][i]
        salary = employee["salary"][i]
        m_id = employee["managerId"][i]


        data_dict[id] = [name, salary, m_id]

    
    emp = []

    for e_id, details in data_dict.items():

        if(details[2] in data_dict and details[1] > data_dict[details[2]][1]):
            emp.append(details[0])

    return pd.DataFrame(emp, columns = ["Employee"])

