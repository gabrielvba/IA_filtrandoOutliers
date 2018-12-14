from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import preprocessing

def cols2numeric(df):
    df.drop("Vin",1,inplace=True)
    df[["City","State","Make", "Model"]] = df[["City","State","Make", "Model"]].astype('category')
    cat_columns = df.select_dtypes(['category']).columns
    df[cat_columns] = df[cat_columns].apply(lambda x: x.cat.codes)
    return df

def preparing_data(csv_name="true_car_listings.csv",to_numeric=True,IQR=True):
    df = pd.read_csv(csv_name)
    if(to_numeric):
        df = cols2numeric(df)
    if(IQR):
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        df = df[~((df < (Q1 - 1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
        
    X = df[["Year","Mileage","City","State","Make","Model"]]
    y = df["Price"]
    
    return X,y

