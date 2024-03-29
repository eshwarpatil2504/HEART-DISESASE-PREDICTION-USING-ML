from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Age = float(request.form['Age'])
    Sex = float(request.form['Sex'])
    trestbps = float(request.form['trestbps'])
    chol = float(request.form['chol'])
    fbs = float(request.form['fbs'])
    restecg = float(request.form['restecg'])
    thalach = float(request.form['thalach'])
    exang = float(request.form['exang'])
    oldpeak = float(request.form['oldpeak'])
    slope = float(request.form['slope'])
    ca = float(request.form['ca'])
    thal = float(request.form['thal'])
    cp = float(request.form['cp'])
    
    result = model.predict([[Age, Sex, trestbps, chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,cp]])
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
