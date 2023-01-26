import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('files/salaries.csv')

print(dataset.head(5))

# Number of examples inside the dataset
print(dataset.shape)

x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)

print(X_train)

# Model assignment
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Visualizes graphically the training
viz_train = plt
viz_train.scatter(X_train, Y_train, color='blue')
viz_train.plot(X_train, regressor.predict(X_train), color='green')
viz_train.title('Salary VS Experience')
viz_train.xlabel('Experience')
viz_train.ylabel('Salary')
viz_train.show()

# Checks if the training was successful with test data
viz_train = plt
viz_train.scatter(X_test, Y_test, color='blue')
viz_train.plot(X_train, regressor.predict(X_train), color='green')
viz_train.title('Salary VS Experience')
viz_train.xlabel('Experience')
viz_train.ylabel('Salary')
viz_train.show()

print(regressor.score(X_test, Y_test))
