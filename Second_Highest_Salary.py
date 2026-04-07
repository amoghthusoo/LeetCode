import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    salaries = set()

    for i in range(len(employee["id"])):
        salaries.add(employee["salary"][i])
    
    salaries = sorted(list(salaries))

    _second_highest_salary = []

    if(len(salaries) <= 1):
        _second_highest_salary.append(None)
    else:
        _second_highest_salary.append(salaries[-2])

    data = {
        "SecondHighestSalary" : _second_highest_salary
    }

    return pd.DataFrame(data)