import plotly
import plotly.express as px
from data import data_lending
import json
import pickle

def count_plots():
    df = data_lending()
    fig = px.bar(x=df["loan_status"].value_counts().index, y=df["loan_status"].value_counts().values)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

    
def amount_plots():
    df = data_lending()
    fig = px.histogram(df, x="loan_amnt", color="loan_status",
                   marginal="box", hover_data=df.columns)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

# def default_plots():
#     df = data_bankmarketing()
#     fig = px.bar(x=df["default"].value_counts().index, y=df["default"].value_counts().values)
#     fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
#     return fig_json