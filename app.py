from flask import Flask, request, jsonify, render_template
import pickle


# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('BP.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

#@app.route('/predict', methods=['POST'])
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Debug input
        age = float(request.form['age'])
        print(f"Received age: {age}")

        # Debug model prediction
        prediction = model.predict([[age]])
        print(f"Prediction: {prediction}")

        result = round(prediction[0], 2)
        return render_template('result.html', prediction_text=f'Predicted Blood Pressure: {result} mmHg')
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred while processing your request."

if __name__ == '__main__':
    app.run(debug=True)
