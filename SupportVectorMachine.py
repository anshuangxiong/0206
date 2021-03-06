#Import Library
from sklearn import svm

#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create SVM classification object
model = svm.svc() # there is various option associated with it, this is simple for classification. You can refer link, for mo# re detail.
# Train the model using the training sets and check score
X = [[150.0], [200.0], [250.0], [300.0], [350.0], [400.0], [600.0]]
y = [6450.0, 7450.0, 8450.0, 9450.0, 11450.0, 15450.0, 18450.0]
x_test = [[280.0]]
model.fit(X, y)
model.score(X, y)

#Predict Output
predicted= model.predict(x_test)