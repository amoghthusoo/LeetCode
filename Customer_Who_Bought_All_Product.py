import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    prod_set = set(product["product_key"])
    intr_dict = dict()

    for i in range(len(customer["customer_id"])):
        
        id = customer["customer_id"][i]
        prod = customer["product_key"][i]

        if(id not in intr_dict):
            intr_dict[id] = {prod}
        else:
            intr_dict[id].add(prod)
        
    
    customer_id = []
    for id, prod in intr_dict.items():
        if(prod == prod_set):
            customer_id.append(id)
    
    return pd.DataFrame(customer_id, columns = ["customer_id"])