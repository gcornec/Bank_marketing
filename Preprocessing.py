def preprocessing(df, var_bin, var_cat):

    import pandas as pd

    #On modifie les variables binaires
    dic_bin = {"yes": 1, "no": 0}
    for col in var_bin:
        df[col+"_bin"] = df[col].map(dic_bin)

    #On opère un one hot encoding sur les variables multi catégorielles (chaque modalité est codée comme une variable)
    for col in var_cat:
        #La commande drop_first permet d'enlever une modalité à chaque variable afin de diminuer la colinéarité entre les variables
        df = pd.get_dummies(df, prefix = col, columns = [col], drop_first= True)

    return df.drop(columns = var_bin, axis = 1)