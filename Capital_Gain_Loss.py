import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:

    stock_dict = {}
    for i in range(len(stocks["stock_name"])):

        stock_name = stocks["stock_name"][i]
        operation = stocks["operation"][i]
        price = stocks["price"][i]

        if(stock_name not in stock_dict):
            stock_dict[stock_name] = 0

        if(operation == "Sell"):
            stock_dict[stock_name] += price
        else:
            stock_dict[stock_name] -= price
        
    
    stock_name = []
    capital_gain_loss = []

    for name, gain_loss in stock_dict.items():
        stock_name.append(name)
        capital_gain_loss.append(gain_loss)
    

    data = {
        "stock_name" : stock_name,
        "capital_gain_loss" : capital_gain_loss
    }

    return pd.DataFrame(data)
        