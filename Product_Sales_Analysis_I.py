import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    
    prod_table_dict = {}

    for i in range(len(product["product_id"])):
        prod_table_dict[product["product_id"][i]] = product["product_name"][i]


    prod_name = []
    year = []
    price = []


    for i in range(len(sales["sale_id"])):

        prod_name.append(prod_table_dict[sales["product_id"][i]])
        year.append(sales["year"][i])
        price.append(sales["price"][i])
    
    data = {
        "product_name" : prod_name,
        "year" : year,
        "price" : price
    }

    return pd.DataFrame(data)

