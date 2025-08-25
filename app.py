from flask import Flask,request
from main import generateCLASSIFIER
import pickle

generateCLASSIFIER()
Classifier=pickle.load(open('model.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return('CLASSIFIER Model Server is running')

@app.route('/predict',methods=['GET'])
def predict():
    temp=request.args.get('temp')
    temp=float(temp)
    data=[[temp]]
    result=Classifier.predict(data)
    result=result(0)
    return(result)

if(__name__=="__main__"):
    app.run(host='0.0.0.0',port=5000,debug=True)
    

