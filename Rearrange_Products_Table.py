import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    
    product_id = []
    store = []
    price = []

    i = 0
    while(i < len(products["product_id"])):
        

        if(not pd.isna(products["store1"][i])):
            product_id.append(products["product_id"][i])
            store.append("store1")
            price.append(products["store1"][i])
        
        if(not pd.isna(products["store2"][i])):
            product_id.append(products["product_id"][i])
            store.append("store2")
            price.append(products["store2"][i])
        
        if(not pd.isna(products["store3"][i])):
            product_id.append(products["product_id"][i])
            store.append("store3")
            price.append(products["store3"][i])
        
        i += 1

    
    data = {
        "product_id" : product_id,
        "store" : store,
        "price" : price
    }

    return pd.DataFrame(data)

