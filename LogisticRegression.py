#Import Library
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create logistic regression object
model = LogisticRegression()
x_train = [[150.0], [200.0], [250.0], [300.0], [350.0], [400.0], [600.0]]
y_train = [6450.0, 7450.0, 8450.0, 9450.0, 11450.0, 15450.0, 18450.0]
x_test = [[280.0]]
# Train the model using the training sets and check score
model.fit(x_train, y_train)
model.score(x_train, y_train)

#Equation coefficient and Intercept
print('Coefficient: n', model.coef_)
print('Intercept: n', model.intercept_)

#Predict Output
predicted= model.predict(x_test)
print(predicted)

# 画图
# 1.真实的点
plt.scatter(x_train, y_train, color='blue')

# 2.拟合的直线
plt.plot(x_train, model.predict(x_train), color='red', linewidth=4)

plt.show()