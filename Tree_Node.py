import pandas as pd

def tree_node(tree: pd.DataFrame) -> pd.DataFrame:
    
    root = None
    U = set()
    internal = set()

    for i in range(len(tree["id"])):

        id = tree["id"][i]
        pid = tree["p_id"][i]


        if(pd.isna(pid)):
            root = id
        else:
            internal.add(pid)
            U.add(id)
    
    internal.discard(root)
    leaf = U.difference(internal)

    id = [root]
    type = ["Root"]

    for e in internal:
        id.append(e)
        type.append("Inner")
    
    for e in leaf:
        id.append(e)
        type.append("Leaf")

    data = {
        "id" : id,
        "type" : type
    }

    return pd.DataFrame(data)