import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

countries = {
    'CO': 1,
    'PE': 2,
    'MX': 3,
    'AR': 4
}

# Defined rules of salary ranges on each region


def getCountryBySalary(salary=float):
    if salary <= 18000:
        return countries['PE']
    elif salary > 18000 and salary <= 25000:
        return countries['AR']
    elif salary > 25000 and salary <= 32000:
        return countries['CO']
    elif salary >= 32000:
        return countries['MX']


# Dataset is converted into a dataframe
dataset = pd.read_csv('files/salaries.csv')
df = pd.DataFrame(dataset)

cols = dataset.shape[1]

# Added Pais column on every record, the country is assigned according
# To the salary range.
df = df.assign(Pais=df['Salario'].apply(getCountryBySalary))

# Plot of Years vs Salary
plt.scatter(df['Aexperiencia'], df['Salario'])
plt.xlabel('Years')
plt.ylabel('Salary')
plt.show()

# Plot of Countries vs Salary
plt.scatter(df['Pais'], df['Salario'])
plt.xlabel('Pais')
plt.ylabel('Salary')
plt.show()

# Defined x and y variables
x = df[['Aexperiencia', 'Pais']]
y = df['Salario']


X_train, X_test, Y_train, Y_test = train_test_split(
    x, y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(X_train, Y_train)

# Visualizes graphically the training
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1, projection='3d')
ax.scatter(X_train['Aexperiencia'], X_train['Pais'], Y_train, color='blue')
ax.scatter(X_train['Aexperiencia'], X_train['Pais'],
           regressor.predict(X_train), color='green')
ax.set_xlabel('Aexperiencia')
ax.set_ylabel('Pais')
ax.set_zlabel('Salary')
plt.show()

# Visualizes graphically the test
fig = plt.figure(dpi=150)
ax = fig.add_subplot(1, 0.5, 1, projection='3d')
ax.scatter(X_test['Aexperiencia'], X_test['Pais'], Y_test, color='red')
ax.scatter(X_train['Aexperiencia'], X_train['Pais'],
           regressor.predict(X_train), color='green')
ax.set_xlabel('Aexperiencia')
ax.set_ylabel('Pais')
ax.set_zlabel('Salary')
plt.show()

print(regressor.score(X_test, Y_test))
