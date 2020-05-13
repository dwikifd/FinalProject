import pickle
from pandas import DataFrame,get_dummies

model = pickle.load(open('finalized_model.sav','rb'))
real_columns = pickle.load(open('real_columns.sav','rb'))
one_hot_columns = pickle.load(open('x_columns.sav','rb'))

def prediction(data):
    df = DataFrame(data,index=[0])
    df = get_dummies(df)
    df = df.reindex(columns=one_hot_columns, fill_value=0)
    hasil1 = model.predict(df)
    if hasil1==0:
        hasil='Fully Paid'
    else:
        hasil='Charged Off'
    return hasil