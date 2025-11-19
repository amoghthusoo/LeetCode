import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    
    intr = []

    for i in range(len(queue["person_id"])):

        turn = queue["turn"][i]
        weight = queue["weight"][i]
        name = queue["person_name"][i]

        intr.append((turn, weight, name))
    
    intr.sort()

    cumm_sum = 0
    i = 0
    while(i < len(intr)):

        cumm_sum += intr[i][1]

        if(cumm_sum > 1000):
            i -= 1
            break

        i += 1
    else:
        i -= 1
        
    person_name = [intr[i][2]]

    data = {
        "person_name" : person_name
    }

    return pd.DataFrame(data)

data = [[5, 'Alice', 1, 1], [4, 'Bob', 2, 5], [3, 'Alex', 3, 2], [6, 'John Cena', 4, 3], [1, 'Winston', 5, 6], [2, 'Marie', 6, 4]]
queue = pd.DataFrame(data, columns=['person_id', 'person_name', 'weight', 'turn']).astype({'person_id':'Int64', 'person_name':'object', 'weight':'Int64', 'turn':'Int64'})

result = last_passenger(queue)
print(result)