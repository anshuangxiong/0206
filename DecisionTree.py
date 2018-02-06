# Import Library
# Import other necessary libraries like pandas, numpy...
from sklearn import tree
import matplotlib.pyplot as plt
X = [[150.0], [200.0], [250.0], [300.0], [350.0], [400.0], [600.0]]
y = [6450.0, 7450.0, 8450.0, 9450.0, 11450.0, 15450.0, 18450.0]
x_test = [[280.0]]
# Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create tree object
model = tree.DecisionTreeClassifier(
    criterion='gini')  # for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini

# model = tree.DecisionTreeRegressor() for regression
# Train the model using the training sets and check score
model.fit(X, y)
model.score(X, y)

# Predict Output
predicted = model.predict(x_test)
print(predicted)

# 画图
# 1.真实的点
plt.scatter(X, y, color='blue')

# 2.拟合的直线
plt.plot(X, model.predict(X), color='red', linewidth=4)

plt.show()