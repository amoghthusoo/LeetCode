import pandas as pd

def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:

    content_id = []
    original_text = []
    converted_text = []

    for i in range(len(user_content["content_id"])):

        cid = user_content["content_id"][i]
        ot : str = user_content["content_text"][i]

        content_id.append(cid)
        original_text.append(ot)

        intr = []
        temp = ot.split()
        for word in temp:

            if(word.isalpha()):
                word = word.capitalize()
                intr.append(word)
            
            elif(word.count("-") == 1 and word.index("-") not in [0, len(word) - 1]):

                word_split = word.split("-")
                f1 = word_split[0]
                f2 = word_split[1]

                f1 = f1.capitalize()
                f2 = f2.capitalize()

                concat = f1 + "-" + f2
                intr.append(concat)
            
            else:

                word = word.capitalize()
                intr.append(word)

        joined = " ".join(intr)

        converted_text.append(joined)
    
    data = {
        "content_id" : content_id,
        "original_text" : original_text,
        "converted_text" : converted_text
    }

    return pd.DataFrame(data)