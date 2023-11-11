import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = [
    {'Name': 'Dell Latitude 5590', 'Price': '$659.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '512 GB (1x 512 GB SSD)', 'Display': '15.6" FHD (1920 x 1080)'},
    {'Name': 'Dell Latitude 5590', 'Price': '$589.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '512 GB (1x 512 GB SSD)', 'Display': '15.6" FHD (1920 x 1080)'},
    {'Name': 'Dell Latitude 7390', 'Price': '$549.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '13.3" FHD (1920 x 1080)'},
    {'Name': 'Dell Latitude 7490', 'Price': '$409.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '14" HD (1366 x 768)'},
    {'Name': 'Dell Latitude 3310 - No OS', 'Price': '$189.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '13.3" HD (1366 x 768)'},
    {'Name': 'Dell Latitude 3310 - No OS', 'Price': '$169.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '13.3" HD (1366 x 768)'},
    {'Name': 'Dell Latitude 5290', 'Price': '$309.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '512 GB (1x 512 GB SSD)', 'Display': '12.5" HD (1366 x 768)'},
    {'Name': 'Dell Latitude 5290 2-In-1 Touch', 'Price': '$469.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '12.3" FHD Touch (1920 x 1080)'},
    {'Name': 'Dell Latitude 5290 2-In-1 Touch', 'Price': '$419.00', 'Memory': '8 GB (1x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '12.3" FHD Touch (1920 x 1080)'},
    {'Name': 'Dell Latitude 5300 2-In-1 Touch', 'Price': '$549.00', 'Memory': '16 GB (2x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '13.3" FHD Touch (1920 x 1080)'},
    {'Name': 'Dell Latitude 5400', 'Price': '$459.00', 'Memory': '16 GB (2x 8GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '14" FHD (1920 x 1080)'},
    {'Name': 'Dell Latitude 5400', 'Price': '$339.00', 'Memory': '16 GB (1x 16GB)', 'Storage': '256 GB (1x 256 GB SSD)', 'Display': '14" FHD (1920 x 1080)'}
]

df = pd.DataFrame(data)

# Convert 'Price' to numerical
df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)

# Extract numerical values from 'Memory' and 'Storage'
df['Memory_GB'] = df['Memory'].str.extract('(\d+)').astype(float)
df['Storage_GB'] = df['Storage'].str.extract('(\d+)').astype(float)

# Extract display size and resolution
df['Display_in'] = df['Display'].str.extract('(\d+\.?\d*)').astype(float)
df['Resolution'] = df['Display'].str.extract('(\d+ x \d+)')

# Create binary features for Touchscreen, 2-in-1, and No OS
df['Touchscreen'] = df['Name'].str.contains('Touch').astype(int)
df['Two_in_One'] = df['Name'].str.contains('2-In-1').astype(int)
df['No_OS'] = df['Name'].str.contains('No OS').astype(int)

# Drop original columns if they are no longer needed
df = df.drop(['Name', 'Memory', 'Storage', 'Display'], axis=1)

# One-hot encode the 'Resolution' column
df = pd.get_dummies(df, columns=['Resolution'])

# Prepare the data
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("Coefficient of Determination (R^2):", r2_score(y_test, y_pred))

# Coefficients
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
