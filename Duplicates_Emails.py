import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    
    visited = set()

    ans = set()

    for i in range(len(person["id"])):

        email = person["email"][i]

        if(email not in visited):
            visited.add(email)
        else:
            ans.add(email)

    return pd.DataFrame(list(ans), columns = ["Email"])