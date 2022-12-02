from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Education =float(request.form['Education'])
    Income =float(request.form['Income'])
    Kidhome =float(request.form['Kidhome'])
    Teenhome =float(request.form['Teenhome'])
    Recency =float(request.form['Recency'])
    MntWines =float(request.form['MntWines'])
    MntFruits =float(request.form['MntFruits'])
    MntMeatProducts =float(request.form['MntMeatProducts'])
    MntFishProducts =float(request.form['MntFishProducts'])
    MntSweetProducts =float(request.form['MntSweetProducts'])
    MntGoldProds =float(request.form['MntGoldProds'])
    NumDealsPurchases =float(request.form['NumDealsPurchases'])
    NumWebPurchases =float(request.form['NumWebPurchases'])
    NumCatalogPurchases =float(request.form['NumCatalogPurchases'])
    NumStorePurchases =float(request.form['NumStorePurchases'])
    NumWebVisitsMonth =float(request.form['NumWebVisitsMonth'])
    AcceptedCmp3 =float(request.form['AcceptedCmp3'])
    AcceptedCmp4 =float(request.form['AcceptedCmp4'])
    AcceptedCmp5 =float(request.form['AcceptedCmp5'])
    AcceptedCmp1 =float(request.form['AcceptedCmp1'])
    AcceptedCmp2 =float(request.form['AcceptedCmp2'])
    Complain =float(request.form['Complain'])
    Response =float(request.form['Response'])
    Age =float(request.form['Age'])
    Spent =float(request.form['Spent'])
    Living_With =float(request.form['Living_With'])
    Children =float(request.form['Children'])
    Family_Size =float(request.form['Family_Size'])
    Is_Parent =float(request.form['Is_Parent'])
    Total_Promos =float(request.form['Total_Promos'])





    result = model.predict([[Education, Income,Kidhome, Teenhome, Recency, MntWines,MntFruits, MntMeatProducts, MntFishProducts, MntSweetProducts,MntGoldProds, NumDealsPurchases, NumWebPurchases,NumCatalogPurchases, NumStorePurchases, NumWebVisitsMonth,
       AcceptedCmp3, AcceptedCmp4, AcceptedCmp5, AcceptedCmp1,
       AcceptedCmp2, Complain, Response, Age, Spent, Living_With,
       Children, Family_Size, Is_Parent, Total_Promos]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)