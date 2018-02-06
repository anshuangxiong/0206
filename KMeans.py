

# Import Library
from sklearn.cluster import KMeans

# Assumed you have, X (attributes) for training data set and x_test(attributes) of test_dataset
# Create KNeighbors classifier object model
model = KMeans(n_clusters=3, random_state=0)
X = [[150.0], [200.0], [250.0], [300.0], [350.0], [400.0], [600.0]]
y = [6450.0, 7450.0, 8450.0, 9450.0, 11450.0, 15450.0, 18450.0]
x_test = [[280.0]]
# Train the model using the training sets and check score
model.fit(X)

# Predict Output
predicted = model.predict(x_test)