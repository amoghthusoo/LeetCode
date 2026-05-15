import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:

    person.sort_values(by = "id", inplace = True)
    person.reset_index(drop=True, inplace=True)
    
    visited = set()

    id_ans = []
    email_ans = []

    for i in range(len(person["id"])):

        id = person["id"][i]
        email = person["email"][i]

        if(email not in visited):
            visited.add(email)
            id_ans.append(id)
            email_ans.append(email)

    person.drop(person.index, inplace = True)
    person["id"] = pd.Series(id_ans)
    person["email"] = pd.Series(email_ans)
