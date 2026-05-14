import pandas as pd

def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:

    student_id = []
    age = []

    for data in student_data:
        student_id.append(data[0])
        age.append(data[1])
    
    data = {
        "student_id" : student_id,
        "age" : age
    }

    return pd.DataFrame(data)