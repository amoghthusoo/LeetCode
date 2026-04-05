import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    
    intr_dict = {}

    for i in range(len(products)):

        p_id = products["product_id"][i]
        n_price = products["new_price"][i]
        c_date = products["change_date"][i]

        if(p_id not in intr_dict):
            intr_dict[p_id] = []

        if(str(c_date) <= "2019-08-16 00:00:00"):
            intr_dict[p_id].append([c_date, n_price])


    for key, vals in intr_dict.items():
        intr_dict[key] = sorted(vals, reverse = True)

    
    data = []

    for key, vals in intr_dict.items():

        if(len(vals) != 0):
            data.append([key, vals[0][1]])
        else:
            data.append([key, 10])
    
    return pd.DataFrame(data, columns = ["product_id", "price"])


data = [[1, 20, '2019-08-14'], [2, 50, '2019-08-14'], [1, 30, '2019-08-15'], [1, 35, '2019-08-16'], [2, 65, '2019-08-17'], [3, 20, '2019-08-18']]
products = pd.DataFrame(data, columns=['product_id', 'new_price', 'change_date']).astype({'product_id':'Int64', 'new_price':'Int64', 'change_date':'datetime64[ns]'})
result = price_at_given_date(products)
print(result)