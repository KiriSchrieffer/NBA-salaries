# Author:Qingyuan
# This file contains functions that do salary prediction.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


# This function accepts a list of assists, points per game
# and 3-point field goal of players,
# use salary cap to train the model
# print the R-squared value
# return a list of predict salary
def predict_salary_usecap(points: list) -> list:
    players = pd.read_csv('players.csv')
    salary = pd.read_csv('salaries_1985to2018 .csv')
    salary_cap = pd.read_csv('salary_cap.csv')

    data_b_cleaned = salary[['player_id', 'season_start', 'salary']].copy()
    merged = data_b_cleaned.merge(salary_cap, left_on='season_start',
                                  right_on='start_season')
    merged = merged[['player_id', 'salary', 'salary_cap']]
    merged = merged.groupby('player_id')[['salary', 'salary_cap']].mean()
    merged['salary_divide_cap'] = merged['salary'] / merged['salary_cap']

    # Filter the data
    players = players[['_id', 'career_AST', 'career_PTS', 'career_FG3%']]

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
    y_train = train['salary_divide_cap']
    x_test = test[['career_AST', 'career_PTS', 'career_FG3%']]
    y_test = test['salary_divide_cap']
    model = LinearRegression()
    model.fit(x_train, y_train)

    # Check the accuracy
    y_pred = model.predict(x_test)
    print("R-squared value for this prediction is " + str(
        r2_score(y_test, y_pred)))

    # Predict the salary
    x_predict = points
    y_predict = model.predict(x_predict)
    return y_predict * 134000000


# This function accepts a list of assists, points per game
# and 3-point field goal of players,
# but does NOT use salary cap to train the model
# print the R-squred value
# return a list of predict salary
def predict_salary(points: list) -> list:
    players = pd.read_csv('players.csv')
    salary = pd.read_csv('salaries_1985to2018 .csv')
    salary_cap = pd.read_csv('salary_cap.csv')

    data_b_cleaned = salary[['player_id', 'season_start', 'salary']].copy()
    merged = data_b_cleaned.merge(salary_cap, left_on='season_start',
                                  right_on='start_season')
    merged = merged[['player_id', 'salary', 'salary_cap']]
    merged = merged.groupby('player_id')[['salary', 'salary_cap']].mean()
    merged['salary_divide_cap'] = merged['salary'] / merged['salary_cap']

    # Filter the data
    players = players[['_id', 'career_AST', 'career_PTS', 'career_FG3%']]

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

    # Check the accuracy
    y_pred = model.predict(x_test)
    print("R-squared value for this prediction is " + str(
        r2_score(y_test, y_pred)))

    # Predict the salary
    x_predict = points
    y_predict = model.predict(x_predict)
    return y_predict
