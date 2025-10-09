import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    
    id = []
    student = []

    for i in range(len(seat["id"])):

        id.append(seat["id"][i])
        student.append(seat["student"][i])

    i = 0
    while(i < len(student)):

        try:
            student[i], student[i + 1] = student[i + 1], student[i]
        except:
            pass
        
        i += 2
    
    data = {
        "id" : id,
        "student" : student
    }

    return pd.DataFrame(data)