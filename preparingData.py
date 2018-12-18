from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing

def drop_toNumeric(df):
    df.drop("City",1,inplace=True)
    df.drop("State",1,inplace=True)
    df[["Make", "Model"]] = df[["Make", "Model"]].astype('category')
    cat_columns = df.select_dtypes(['category']).columns
    df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
    return df


def preparing_data(csv_name="final.csv"):
    df = pd.read_csv(csv_name)
    df = drop_toNumeric(df)
        
    X = df[["Year","Mileage","Make","Model"]]
    y = df["Price"]
    
    return X,y

