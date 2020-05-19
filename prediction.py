import pickle
import pandas as pd
from pandas import DataFrame,get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
real_columns = pickle.load(open('real_columns.sav','rb'))
one_hot_columns = pickle.load(open('x_columns.sav','rb'))

def prediction(data):
    columns = ["loan_amnt", "term", "int_rate","installment","sub_grade","home_ownership","annual_inc",
    "verification_status","dti","earliest_credit_year","open_acc","pub_rec","revol_bal","revol_util","total_acc",
    "mort_acc","application_type","initial_list_status","purpose","zip_code"]
    df = DataFrame(data, columns=columns, index=[0])
    df['term'] = df['term'].apply(lambda term: int(term[:3]))
    subgrade_dummies = pd.get_dummies(df['sub_grade'],drop_first=True)
    df = pd.concat([df.drop('sub_grade',axis=1),subgrade_dummies],axis=1)
    dummies = pd.get_dummies(df[['verification_status', 'application_type','initial_list_status','purpose' ]],drop_first=True)
    df = df.drop(['verification_status', 'application_type','initial_list_status','purpose'],axis=1)
    df = pd.concat([df,dummies],axis=1)
    dummies = pd.get_dummies(df['home_ownership'],drop_first=True)
    df = df.drop('home_ownership',axis=1)
    df = pd.concat([df,dummies],axis=1)
    dummies = pd.get_dummies(df['zip_code'],drop_first=True)
    df = df.drop(['zip_code'],axis=1)
    df = pd.concat([df,dummies],axis=1)
    # df = get_dummies(df, drop_first=True)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil1 = model.predict(df)
    if hasil1==0:
        hasil='Fully Paid'
    else:
        hasil='Charged Off'
    return hasil