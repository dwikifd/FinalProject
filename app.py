from flask import Flask,render_template,request
from prediction import prediction
from data import data_lending
from plots import count_plots, amount_plots

## translate Flask to python object
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        hasil = prediction(data)
        return render_template('result.html', hasil_prediction=hasil)
    return render_template('prediction.html')

@app.route('/data')
def data():
    data = data_lending()
    return render_template('table_data.html', data=data)

@app.route('/plots')
def plots():
    data1 = count_plots()
    data2 = amount_plots()
    return render_template('plots.html', data1=data1, data2=data2)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=1111)