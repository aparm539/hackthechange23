import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pickle

laptop_details = [
    {'Name': 'ASUS Chromebook C204', 'CPU': 'Intel Celeron N4020', 'Display Size': '11.6"', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '4GB', 'Storage': '32GB', 'Storage Type': 'Storage type not specified', 'OS': 'Chrome OS', 'Price': '$159.20'},
    {'Name': 'ASUS TUF Gaming F15 Gaming Laptop', 'CPU': 'Intel Core i5-11400H', 'Display Size': '15.6”', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': '144Hz', 'RAM': '8GB', 'Storage': '512GB', 'Storage Type': 'PCIe SSD Gen 3', 'OS': 'Windows 11', 'Price': '$660.78'},
    {'Name': 'ASUS VivoBook 15 X515 Thin and Light Laptop', 'CPU': 'CPU not specified', 'Display Size': '15.6”', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '4GB', 'Storage': '128GB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$324.57'},
    {'Name': 'ASUS ROG Strix G15 (2022) Gaming Laptop', 'CPU': 'AMD Ryzen 7 6800H', 'Display Size': '15.6”', 'Resolution': 'WQHD', 'Display Type': 'IPS', 'Refresh Rate': '165Hz', 'RAM': '16GB', 'Storage': '1TB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$1,319.20'},
    {'Name': 'ASUS TUF Gaming A15 (2023) Gaming Laptop', 'CPU': 'AMD Ryzen 9 7940HS', 'Display Size': '15.6”', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': '144Hz', 'RAM': '16GB', 'Storage': '512GB', 'Storage Type': 'SSD', 'OS': 'Windows 11', 'Price': '$1,424.05'},
    {'Name': 'ASUS Vivobook 15 Laptop', 'CPU': 'Intel Core i7-1355U', 'Display Size': '15.6”', 'Resolution': 'FHD', 'Display Type': 'VA', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '16GB', 'Storage': '1TB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$929.07'},
    {'Name': 'Apple 2020 MacBook Air Laptop: Apple M1 Chip', 'CPU': 'CPU not specified', 'Display Size': '13"', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': '256GB', 'Storage Type': 'SSD', 'OS': 'macOS', 'Price': '$1,045.87'},
    {'Name': 'ASUS Vivobook Go 15 Laptop', 'CPU': 'AMD Ryzen 5 7520U', 'Display Size': '15.6”', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '16GB', 'Storage': '512GB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$650.07'},
    {'Name': 'ASUS Chromebook Flip CX3', 'CPU': 'Intel Core i3-1110G', 'Display Size': '14"', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': 'Storage not specified', 'Storage Type': 'SSD', 'OS': 'Chrome OS', 'Price': '$468.36'},
    {'Name': 'ROG Zephyrus G14 (2022) Ultra Slim Gaming Laptop', 'CPU': 'AMD Ryzen 9 6900HS', 'Display Size': '14”', 'Resolution': 'Resolution not specified', 'Display Type': 'VA', 'Refresh Rate': '144Hz', 'RAM': '16GB', 'Storage': '1TB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$1,394.07'},
    {'Name': 'Acer Chromebook 3', 'CPU': 'CPU not specified', 'Display Size': '14"', 'Resolution': 'Resolution not specified', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '4GB', 'Storage': 'Storage not specified', 'Storage Type': 'Storage type not specified', 'OS': 'Chrome OS', 'Price': '$231.99'},
    {'Name': 'Apple 2023 MacBook Air Laptop with M2 chip: 15.3-inch Liquid Retina Display', 'CPU': 'CPU not specified', 'Display Size': 'Display not specified', 'Resolution': '1080p', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': '256GB', 'Storage Type': 'SSD', 'OS': 'macOS', 'Price': '$1,246.95'},
    {'Name': 'ASUS VivoBook 14 X415 Thin and Light Laptop', 'CPU': 'Intel Core i3-1115G', 'Display Size': '14”', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': 'Storage not specified', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$407.14'},
    {'Name': 'ASUS Vivobook Go 14 Laptop', 'CPU': 'AMD Ryzen 5 7520U', 'Display Size': '14”', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': '512GB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$494.99'},
    {'Name': 'Acer Aspire 3', 'CPU': 'AMD Ryzen 3 7320U', 'Display Size': '15.6"', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': 'Storage not specified', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$406.10'},
    {'Name': 'ASUS Laptop L510 Ultra Thin Laptop', 'CPU': 'Intel Celeron N4020', 'Display Size': '15.6”', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '4GB', 'Storage': 'Storage not specified', 'Storage Type': 'Storage type not specified', 'OS': 'Windows 11 Home', 'Price': '$226.88'},
    {'Name': 'ASUS Chromebook CX1', 'CPU': 'Intel Celeron N4500', 'Display Size': '15.6"', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': 'Storage not specified', 'Storage Type': 'eMMC', 'OS': 'Chrome OS', 'Price': '$330.14'},
    {'Name': 'Samsung Galaxy Book Go S-Mode 14" Laptop - Qualcomm Snapdragon 7c', 'CPU': 'CPU not specified', 'Display Size': 'Display not specified', 'Resolution': 'Resolution not specified', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '4GB', 'Storage': '128GB', 'Storage Type': 'SSD', 'OS': 'OS not specified', 'Price': '$308.06'},
    {'Name': 'Acer Chromebook 315', 'CPU': 'Intel Celeron N4020', 'Display Size': '15.6"', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '4GB', 'Storage': 'Storage not specified', 'Storage Type': 'eMMC', 'OS': 'Chrome OS', 'Price': '$205.55'},
    {'Name': 'Apple 2020 MacBook Air Laptop: Apple M1 Chip', 'CPU': 'CPU not specified', 'Display Size': 'Display not specified', 'Resolution': 'HD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': '256GB', 'Storage Type': 'SSD', 'OS': 'macOS', 'Price': '$1,069.69'},
    {'Name': 'Acer Aspire 3 15.6" FHD Laptop', 'CPU': 'CPU not specified', 'Display Size': 'Display not specified', 'Resolution': 'Resolution not specified', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '16GB', 'Storage': '512GB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$743.99'},
    {'Name': 'ASUS VivoBook 15X OLED Laptop', 'CPU': 'Intel Core i5-12500H', 'Display Size': '15.6”', 'Resolution': 'FHD', 'Display Type': 'OLED', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': '512GB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$759.05'},
    {'Name': 'ASUS VivoBook Flip 14 Thin and Light 2-in-1 Laptop', 'CPU': 'Intel Core i5-1135G', 'Display Size': '14”', 'Resolution': 'FHD', 'Display Type': 'Display type not specified', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '8GB', 'Storage': '256GB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$641.71'},
    {'Name': 'ASUS Zenbook S 13 OLED Ultra Laptop 2023', 'CPU': 'CPU not specified', 'Display Size': '13.3”', 'Resolution': 'Resolution not specified', 'Display Type': 'VA', 'Refresh Rate': 'Refresh rate not specified', 'RAM': '16GB', 'Storage': '1TB', 'Storage Type': 'SSD', 'OS': 'Windows 11 Home', 'Price': '$1,329.40'}
]
# Convert the data to a DataFrame
df = pd.DataFrame(laptop_details)

# Data preprocessing
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)
df['RAM'] = df['RAM'].str.replace('GB', '').astype(int)
df['Storage'] = df['Storage'].str.replace('GB', '').replace('TB', '000', regex=True).replace('Storage not specified', '0').astype(float)
df['Display Size'] = df['Display Size'].str.replace(r'[^\d.]+', '', regex=True)
df['Display Size'] = df['Display Size'].replace('', '0').astype(float)

# Convert 'Refresh Rate' to numeric
df['Refresh Rate'] = df['Refresh Rate'].str.extract('(\d+)').fillna(0).astype(int)

# Extract CPU Brand and Model
df['CPU Brand'] = df['CPU'].apply(lambda x: x.split()[0] if 'CPU not specified' not in x else 'Unknown')
df['CPU Model'] = df['CPU'].apply(lambda x: ' '.join(x.split()[1:]) if 'CPU not specified' not in x else 'Unknown')

# Prepare the features (X) and target (y)
X = df.drop(['Price', 'Name', 'CPU'], axis=1)  # Exclude 'Name' and 'CPU' from features
y = df['Price']

# Specify the categorical features for one-hot encoding
categorical_features = ['OS', 'Display Type', 'Resolution', 'CPU Brand', 'CPU Model', 'Storage Type']
categorical_features = [col for col in categorical_features if col in X.columns]

# One Hot Encoding for categorical variables
one_hot = OneHotEncoder(handle_unknown='ignore')  # Set handle_unknown to 'ignore'
transformer = ColumnTransformer([("one_hot", one_hot, categorical_features)], remainder="passthrough")



# Create a model pipeline
model = Pipeline(steps=[('transformer', transformer), ('model', RandomForestRegressor())])

# Splitting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
print("Model Root Mean Squared Error:", mean_squared_error(y_test, y_pred, squared=False))

# Function to make predictions
def predict_price(input_data):
    input_df = pd.DataFrame([input_data])
    return model.predict(input_df)[0]

# Example usage
predicted_price = predict_price({'OS': 'Windows 10', 'Display Type': 'IPS', 'Resolution': 'FHD', 'CPU Brand': 'Intel', 'CPU Model': 'i7', 'RAM': 16, 'Storage': 512, 'Display Size': 15.6, 'Refresh Rate': 144,'Storage Type': 'SSD'})
print("Predicted Price:", predicted_price)

with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)