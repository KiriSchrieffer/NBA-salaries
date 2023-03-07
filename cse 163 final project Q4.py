import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# Read the data
players = pd.read_csv(r'C:\Users\qingy\Downloads\players.csv')
salary = pd.read_csv(r'C:\Users\qingy\Downloads\salaries_1985to2018.csv')

# Filter the data
players = players[['_id', 'career_AST', 'career_FG%', 'career_FG3%']]
salary = salary[['player_id', 'salary']]

# Merge the two data
data = pd.merge(players, salary, left_on='_id', right_on='player_id')

# Drop the duplicate column
data = data.drop(columns=['_id'])

# Drop the rows with missing values
data = data.dropna()

# Drop rows with '-'
data = data[data['career_AST'] != '-']
data = data[data['career_FG%'] != '-']
data = data[data['career_FG3%'] != '-']

# Convert the data type
data['career_AST'] = data['career_AST'].astype('float')
data['career_FG%'] = data['career_FG%'].astype('float')
data['career_FG3%'] = data['career_FG3%'].astype('float')
data['salary'] = data['salary'].astype('float')

# Split the data into training set and testing set
train, test = train_test_split(data, test_size=0.2)

# Train the model
x_train = train[['career_AST', 'career_FG%', 'career_FG3%']]
y_train = train['salary']
x_test = test[['career_AST', 'career_FG%', 'career_FG3%']]
y_test = test['salary']
model = LinearRegression()
model.fit(x_train, y_train)

# Predict the salary
x_predict = pd.DataFrame({'career_AST': [3.5, 4.5, 5.5], 'career_FG%': [45, 45, 45], 'career_FG3%': [35, 35, 35]})
y_predict = model.predict(x_predict)
print(y_predict)

# Check the accuracy
y_pred = model.predict(x_test)
print(r2_score(y_test, y_pred))

# The result shows that the model is not very accurate, the accuracy is only 0.1.