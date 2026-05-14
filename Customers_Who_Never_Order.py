import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    all_customers_dict = dict()

    for i in range(len(customers["id"])):

        id = customers["id"][i]
        name = customers["name"][i]

        all_customers_dict[id] = name



    all_customers = set(customers["id"])
    customers_who_order = set(orders["customerId"])
    customers_who_never_order = all_customers.difference(customers_who_order)

    ans = []
    for cust in customers_who_never_order:
        ans.append(all_customers_dict[cust])

    return pd.DataFrame(ans, columns = ["Customers"])