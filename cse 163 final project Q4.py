import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import numpy as np

# Read the data
players = pd.read_csv(r'C:\Users\qingy\Downloads\players.csv')
salary = pd.read_csv(r'C:\Users\qingy\Downloads\salaries_1985to2018.csv')
salary_cap = pd.read_csv('salary_cap.csv')
test_players = pd.read_csv(r'D:\qingy\Documents\nba_player.csv')

data_a_cleaned = players[['_id', 'career_PTS', 'name']].copy()
data_b_cleaned = salary[['player_id', 'season_start', 'salary']].copy()
merged = data_b_cleaned.merge(salary_cap, left_on='season_start',
                              right_on='start_season')
merged = merged[['player_id', 'salary', 'salary_cap']]
merged = merged.groupby('player_id')[['salary', 'salary_cap']].mean()
merged['salary_divide_cap'] = merged['salary'] / merged['salary_cap']

# Filter the data
players = players[['_id', 'career_AST', 'career_PTS', 'career_FG3%']]
salary = salary[['player_id', 'salary']]

# Merge the two data
data = pd.merge(players, merged, left_on='_id', right_on='player_id')

# Drop the duplicate column
data = data.drop(columns=['_id'])

# Drop the rows with missing values
data = data.dropna()

# Drop rows with '-'
data = data[data['career_AST'] != '-']
data = data[data['career_PTS'] != '-']
data = data[data['career_FG3%'] != '-']

# Convert the data type
data['career_AST'] = data['career_AST'].astype('float')
data['careerPTS'] = data['career_PTS'].astype('float')
data['career_FG3%'] = data['career_FG3%'].astype('float')
data['salary'] = data['salary'].astype('float')

# Drop rows career_FG3% is 0 or 100
data = data[(data['career_FG3%'] != 0) & (data['career_FG3%'] != 100)]

# Split the data into training set and testing set
train, test = train_test_split(data, test_size=0.2)

# Train the model
x_train = train[['career_AST', 'career_PTS', 'career_FG3%']]
y_train = train['salary']
x_test = test[['career_AST', 'career_PTS', 'career_FG3%']]
y_test = test['salary']
model = LinearRegression()
model.fit(x_train, y_train)

# Predict the salary
x_predict = test_players[['career_AST', 'career_PTS', 'career_FG3%']]
y_predict = model.predict(x_predict)
print(y_predict)
r_error = abs(y_predict - test_players['salary']) / y_predict * 100
print(r_error)
print(len(r_error[r_error <= 50]) / len(r_error) * 100)

# plot scatter
# players name as x axis, salary as y axis, put predicted salary and actual salary on the same plot
plt.scatter(test_players['name'], test_players['salary'], label='actual salary')
plt.scatter(test_players['name'], y_predict, label='predicted salary')
plt.xticks(rotation=90)
plt.legend()
plt.show()

# Check the accuracy
y_pred = model.predict(x_test)
print(r2_score(y_test, y_pred))

# Train the model
x_train = train[['career_AST', 'career_PTS', 'career_FG3%']]
y_train = train['salary_divide_cap']
x_test = test[['career_AST', 'career_PTS', 'career_FG3%']]
y_test = test['salary_divide_cap']
model = LinearRegression()
model.fit(x_train, y_train)

# Predict the salary
x_predict = test_players[['career_AST', 'career_PTS', 'career_FG3%']]
y_predict = model.predict(x_predict)
print(y_predict * 134000000)
r_error = abs(y_predict * 134000000 - test_players['salary']) / (y_predict * 134000000) * 100
print(r_error)
print(len(r_error[r_error <= 50]) / len(r_error) * 100)

# plot scatter
# players name as x axis, salary as y axis, put predicted salary and actual salary on the same plot
plt.figure(figsize=(50, 50))
plt.scatter(test_players['name'], test_players['salary'], label='actual salary')
plt.scatter(test_players['name'], y_predict * 134000000, label='predicted salary')
plt.xticks(rotation=90)
plt.legend()
plt.show()

# Check the accuracy
y_pred = model.predict(x_test)
print(r2_score(y_test, y_pred))
