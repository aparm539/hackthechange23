from flask import Flask, jsonify, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Load your trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('form.html')  # Render the HTML form

@app.route('/predict_price', methods=['POST'])
def predict_price():
    # Extract data from form
    os = request.form.get('os', 'Unknown OS')
    display_type = request.form.get('display_type', 'Unknown Display Type')
    resolution = request.form.get('resolution', 'Unknown Resolution')
    cpu_brand = request.form.get('cpu_brand', 'Unknown CPU Brand')
    cpu_model = request.form.get('cpu_model', 'Unknown CPU Model')
    ram = request.form.get('ram', 0)
    storage = request.form.get('storage', 0)
    display_size = request.form.get('display_size', 0)
    refresh_rate = request.form.get('refresh_rate', 0)
    storage_type = request.form.get('storage_type', 'Unknown Storage Type')

    input_data = {
        'OS': [os],
        'Display Type': [display_type],
        'Resolution': [resolution],
        'CPU Brand': [cpu_brand],
        'CPU Model': [cpu_model],
        'RAM': [ram],
        'Storage': [storage],
        'Display Size': [display_size],
        'Refresh Rate': [refresh_rate],
        'Storage Type': [storage_type]
    }

    # Convert to DataFrame with an explicit index
    input_df = pd.DataFrame.from_dict(input_data, orient='columns', dtype=None)
    input_df.index = [0]  # Setting the index to 0 for a single row DataFrame

    # Make prediction
    predicted_price = model.predict(input_df)[0]
    return jsonify({'predicted_price': predicted_price})


if __name__ == '__main__':
    app.run(debug=True)
