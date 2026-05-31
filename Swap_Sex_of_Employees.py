import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    
    id = []
    name = []
    sex = []
    _salary = []

    for i in range(len(salary["id"])):

        id.append(salary["id"][i])
        name.append(salary["name"][i])
        
        if(salary["sex"][i] == "m"):
            sex.append("f")
        else:
            sex.append("m")

    
        _salary.append(salary["salary"][i])
    

    data = {
        "id" : id,
        "name" : name,
        "sex" : sex,
        "salary" : _salary
    }

    return pd.DataFrame(data)