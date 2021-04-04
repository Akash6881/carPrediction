from flask import Flask,render_template,request
import pickle
from flask import Response





app = Flask(__name__)


model = pickle.load(open('my_random_forrest_on_car.pkl','rb'))

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':

        year = int(request.form['Year'])
        age_of_car = 2021 - year

        present_price = float(request.form['Present_Price'])
        kms_driven = int(request.form['Kms_Driven'])
        owner = int(request.form['Owner'])

        fuel_type = request.form['Fuel_Type_Petrol']

        if(fuel_type == 'Petrol'):
            fuel_type_petrol = 1
            fuel_type_diesel = 0
        elif(fuel_type == 'Diesel'):
            fuel_type_petrol = 0
            fuel_type_diesel = 1
        else :
            fuel_type_petrol = 0
            fuel_type_diesel = 0

        seller_type = request.form['Seller_Type_Individual']
        if(seller_type == 'Individual'):
            seller_type_individual = 1
        else:
            seller_type_individual = 0

        transmission = request.form['Transmission_Mannual']
        if(transmission == 'Manual'):
            trans_manual = 1
        else:
            trans_manual = 0



        prediction = model.predict([[present_price, kms_driven, owner, age_of_car, fuel_type_diesel, fuel_type_petrol, seller_type_individual, trans_manual]])

        output = round(prediction[0], 2)

        return render_template('index.html', prediction_text="You Can Sell The Car at {}".format(output))












if __name__=="__main__":
    app.run(port=7000,debug=True)