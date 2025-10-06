import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    dept_dict = {}

    for i in range(len(department)):
        id = department["id"][i]
        name = department["name"][i]

        dept_dict[id] = name
    
    intr_dict = {}

    for i in range(len(employee["id"])):

        name = employee["name"][i]
        salary = employee["salary"][i]
        d_id = employee["departmentId"][i]

        if(d_id not in intr_dict):
            intr_dict[d_id] = []

        intr_dict[d_id].append([salary, name])

    
    for key, vals in intr_dict.items():
        intr_dict[key] = sorted(vals, reverse = True)

    
    data = []
    for key, vals in intr_dict.items():

        highest = vals[0][0]

        i = 0
        while(i < len(vals) and vals[i][0] == highest):
            
            data.append([dept_dict[key], vals[i][1], highest])
            
            i += 1
        
    
    return pd.DataFrame(data, columns = ["Department", "Employee", "Salary"])

data = [[1, 'Joe', 70000, 1], [2, 'Jim', 90000, 1], [3, 'Henry', 80000, 2], [4, 'Sam', 60000, 2], [5, 'Max', 90000, 1]]
employee = pd.DataFrame(data, columns=['id', 'name', 'salary', 'departmentId']).astype({'id':'Int64', 'name':'object', 'salary':'Int64', 'departmentId':'Int64'})
data = [[1, 'IT'], [2, 'Sales']]
department = pd.DataFrame(data, columns=['id', 'name']).astype({'id':'Int64', 'name':'object'})

result = department_highest_salary(employee, department)
print(result)

