import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    salaries = set()

    for i in range(len(employee["id"])):
        salaries.add(employee["salary"][i])
    
    salaries = sorted(list(salaries))

    _second_highest_salary = []

    if(len(salaries) < N or N <= 0):
        _second_highest_salary.append(None)
    else:
        _second_highest_salary.append(salaries[-N])

    data = {
        f"getNthHighestSalary({N})" : _second_highest_salary
    }

    return pd.DataFrame(data)