# -*- coding = utf-8 -*-
# @Time : 2023/3/6 下午 9:23
# @Author : Randy
# @File : Predictor.py
# @Software : PyCharm
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


def salary_avg_points(data_a: pd.DataFrame, data_b: pd.DataFrame) -> None:
    data_a_cleaned = data_a[['_id', 'career_PTS', 'height', 'weight', 'name', 'career_FG3%']].copy()
    data_b_cleaned = data_b[['player_id', 'salary']].copy()
    # average career salary
    merged = _avg_career_salary(data_a_cleaned, data_b_cleaned)
    # convert the height into cm
    chart = alt.Chart(merged).mark_circle(size=30).encode(
        x='career_PTS',
        y='salary',
        tooltip=['name', 'career_PTS', 'height', 'weight'],
    ).properties(width=400, height=400, title='Career Average Points V.S Salary').interactive()
    chart.save('chart.html')


def salary_divide_salary_cap(data_a: pd.DataFrame, data_b: pd.DataFrame, salary_cap: pd.DataFrame) -> None:
    data_a_cleaned = data_a[['_id', 'career_PTS', 'name']].copy()
    data_b_cleaned = data_b[['player_id', 'season_start', 'salary']].copy()
    merged = data_b_cleaned.merge(salary_cap, left_on='season_start',
                                  right_on='start_season')
    merged = merged[['player_id', 'salary', 'salary_cap']]
    merged = merged.groupby('player_id')[['salary', 'salary_cap']].mean()
    merged['salary_divide_cap'] = merged['salary'] / merged['salary_cap']
    ability = merged.merge(data_a_cleaned, left_on='player_id', right_on='_id')
    chart3 = alt.Chart(ability).mark_circle(size=20).encode(
        x='career_PTS',
        y='salary_divide_cap',
        tooltip=['salary', 'salary_cap', 'name']
    ).interactive()
    chart3.save('chart3.html')


def avg_fg3_salary(data_a: pd.DataFrame, data_b: pd.DataFrame) -> None:
    data_a_cleaned = data_a[['_id', 'career_PTS', 'height', 'name', 'career_FG3%', 'weight']].copy()
    data_b_cleaned = data_b[['player_id', 'salary']].copy()
    merged = _avg_career_salary(data_a_cleaned, data_b_cleaned)
    chart2 = alt.Chart(merged).mark_circle(size=20).encode(
        alt.X(alt.repeat('column'), type='quantitative'),
        alt.Y(alt.repeat('row'), type='quantitative'),
        tooltip=['name', 'career_PTS', 'height', 'weight']
    ).properties(height=250, width=250).repeat(
        column=['height', 'career_PTS', 'career_FG3%'],
        row=['salary']
    ).interactive()
    chart2.save("chart2.html")


def salary_in_cap_3fg(data_a: pd.DataFrame, data_b: pd.DataFrame, salary_cap: pd.DataFrame):
    data_a_cleaned = data_a[['_id', 'career_FG3%', 'name']].copy()
    data_b_cleaned = data_b[['player_id', 'season_start', 'salary']].copy()
    merged = data_b_cleaned.merge(salary_cap, left_on='season_start',
                                  right_on='start_season')
    merged = merged[['player_id', 'salary', 'salary_cap']]
    merged = merged.groupby('player_id')[['salary', 'salary_cap']].mean()
    merged['salary_divide_cap'] = merged['salary'] / merged['salary_cap']
    ability = merged.merge(data_a_cleaned, left_on='player_id', right_on='_id')
    chart4 = alt.Chart(ability).mark_circle(size=20).encode(
        x='career_FG3%',
        y='salary_divide_cap',
        tooltip=['name']
    ).interactive()
    chart4.save('chart4.html')



def _avg_career_salary(data_a: pd.DataFrame,
                       data_b: pd.DataFrame) -> pd.DataFrame:
    """
    :rtype: pd.DataFrame
    Help merge and calculate the career average salary
    with other attributes
    """
    career_salary = data_b.groupby('player_id')['salary'].mean()
    merged = data_a.merge(career_salary, left_on="_id",
                          right_on="player_id")
    merged['height'] = merged['height'].apply(_converting_machine)
    return merged


def _converting_machine(input_data):
    feet, inches = input_data.split("-")
    return 2.54 * (int(feet) * 12 + int(inches))
