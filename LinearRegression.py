from sklearn import linear_model

#Import Library
#Import other necessary libraries like pandas, numpy...
from sklearn import linear_model
import matplotlib.pyplot as plt
#Load Train and Test datasets
#Identify feature and response variable(s) and values must be numeric and numpy arrays
#x_train=input_variables_values_training_datasets
#y_train=target_variables_values_training_datasets
#x_test=input_variables_values_test_datasets

x_train = [[150.0], [200.0], [250.0], [300.0], [350.0], [400.0], [600.0]]
# x_train = [150.0, 200.0, 250.0, 300.0, 350.0, 400.0, 600.0]
y_train = [6450.0, 7450.0, 8450.0, 9450.0, 11450.0, 15450.0, 18450.0]
x_test = [[280.0]]
# x_test = [280.0]
# Create linear regression object
linear = linear_model.LinearRegression()

# Train the model using the training sets and check score
# 拟合
linear.fit(x_train, y_train)
linear.score(x_train, y_train)

#Equation coefficient and Intercept
print('Coefficient: n系数', linear.coef_) #系数
print('Intercept: n截距', linear.intercept_) # 截距

#Predict Output
predicted= linear.predict(x_test)
print(predicted)

# 画图
# 1.真实的点
plt.scatter(x_train, y_train, color='blue')

# 2.拟合的直线
plt.plot(x_train, linear.predict(x_train), color='red', linewidth=4)

plt.show()