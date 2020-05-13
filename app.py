from flask import Flask,render_template,request
from prediction import prediction
from cleaning_data import data_lending

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

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=1111)