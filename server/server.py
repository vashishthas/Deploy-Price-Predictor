from flask import Flask, request, jsonify
import util

app=Flask(__name__)
 

@app.route('/hello')
def hello():
    return 'Hi!'

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response=jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    print(util.get_estimated_price(location,sqft,bhk,bath))

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__=='__main__':
    util.load_saved_artifacts()
    print('Strating Python Flask server for Home Price Prediction')
    app.run()