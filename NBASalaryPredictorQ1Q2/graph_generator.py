'''
Name: Runlin He
Section: AI
This file is for generating the Q1 and Q2 related graph
based on three dataset as DataFrame.
We use pandas and altair library.
'''
import pandas as pd
import altair as alt


def salary_avg_points(data_a: pd.DataFrame, data_b: pd.DataFrame) -> None:
    '''
    :param data_a: DataFrame, including player's basic information except salary
    :param data_b: DataFrame, including player's salary from 1985 to 2018
    Take two DataFrame as parameters and generate a html format file for graphing
    the relationship between NBA player's salary and points get per game.
    '''
    player_info = ['_id', 'career_PTS', 'height', 'weight', 'name', 'career_FG3%']
    data_a_cleaned = data_a[player_info].copy()
    data_b_cleaned = data_b[['player_id', 'salary']].copy()
    # average career salary
    merged = _avg_career_salary(data_a_cleaned, data_b_cleaned)
    # convert the height into cm
    tool_hints = ['name', 'career_PTS', 'height', 'weight']
    chart = alt.Chart(merged).mark_circle(size=30)\
        .encode(x='career_PTS', y='salary', tooltip=tool_hints,)\
        .properties(width=400, height=400,
                    title='Career Average Points V.S Salary')\
        .interactive()
    chart.save('chart.html')


def salary_divide_salary_cap(data_a: pd.DataFrame, data_b: pd.DataFrame,
                             salary_cap: pd.DataFrame) -> None:
    '''
    :param data_a: pd.DataFrame, including player's information except salary
    :param data_b: pd.DataFrame, including player's salary and name
    :param salary_cap: pd.DataFrame, including each year's salary cap
    :return: None
    Take three parameters and graph the relationship between
    player's ability (salary divide by salary cap) and scoring ability
    '''
    data_a_cleaned = data_a[['_id', 'career_PTS', 'name']].copy()
    ability = _player_ability_salary(data_a_cleaned, data_b, salary_cap)
    tools = ['salary', 'salary_cap', 'name']
    chart3 = alt.Chart(ability).mark_circle(size=20)\
        .encode(x='career_PTS', y='salary_divide_cap', tooltip=tools)\
        .interactive()
    chart3.save('chart3.html')


def avg_fg3_score_height_salary(data_a: pd.DataFrame,
                                data_b: pd.DataFrame) -> None:
    '''
    :param data_a: pd.DataFrame, including player's information except salary
    :param data_b: pd.DataFrame, including player's salary and name
    :return: None
    Take two DataFrame as parameters and graph the relationship between
    each attribute with salary
    '''
    player_infos = ['_id', 'career_PTS', 'height',
                    'name', 'career_FG3%', 'weight']
    data_a_cleaned = data_a[player_infos].copy()
    data_b_cleaned = data_b[['player_id', 'salary']].copy()
    merged = _avg_career_salary(data_a_cleaned, data_b_cleaned)
    tool_hint = ['name', 'career_PTS', 'height', 'weight']
    chart2 = alt.Chart(merged).mark_circle(size=20)\
        .encode(alt.X(alt.repeat('column'), type='quantitative'),
                alt.Y(alt.repeat('row'), type='quantitative'),
                tooltip=tool_hint)\
        .properties(height=250, width=250).repeat(
        column=['height', 'career_PTS', 'career_FG3%'],
        row=['salary']
    ).interactive()
    chart2.save("chart2.html")


def salary_in_cap_3fg(data_a: pd.DataFrame, data_b: pd.DataFrame,
                      salary_cap: pd.DataFrame) -> None:
    '''
    :param data_a: pd.DataFrame, including player's information except salary
    :param data_b: pd.DataFrame, including player's salary and name
    :param salary_cap: pd.DataFrame, including each year's salary cap
    :return:  None
    '''
    data_a_cleaned = data_a[['_id', 'career_FG3%', 'name']].copy()
    ability = _player_ability_salary(data_a_cleaned, data_b, salary_cap)
    chart4 = alt.Chart(ability).mark_circle(size=20).encode(
        x='career_FG3%',
        y='salary_divide_cap',
        tooltip=['name']
    ).interactive()
    chart4.save('chart4.html')


def _player_ability_salary(data_a_cleaned: pd.DataFrame,
                           data_b: pd.DataFrame,
                           salary_cap: pd.DataFrame) -> pd.DataFrame:
    '''
    :param data_a_cleaned: pd.DataFrame,
    including player's information except salary
    :param data_b: pd.DataFrame, including player's salary and name
    :param salary_cap: pd.DataFrame, including each year's salary cap
    :return: pd.DataFrame
    This function will merge three dataset into one which stands for
    player's salary divide by their salary cap.
    Return the merged DataFrame.
    '''
    data_b_cleaned = data_b[['player_id', 'season_start', 'salary']].copy()
    merged = data_b_cleaned.merge(salary_cap, left_on='season_start',
                                  right_on='start_season')
    merged = merged[['player_id', 'salary', 'salary_cap']]
    merged = merged.groupby('player_id')[['salary', 'salary_cap']].mean()
    merged['salary_divide_cap'] = merged['salary'] / merged['salary_cap']
    ability = merged.merge(data_a_cleaned, left_on='player_id', right_on='_id')
    return ability


def _avg_career_salary(data_a: pd.DataFrame,
                       data_b: pd.DataFrame) -> pd.DataFrame:
    '''
    Take two DataFrame as parameter, a for player's scoring information
    and  database b for  salary
    Help merge and calculate the career average salary with other attributes
    Return the merged DataFrame
    '''
    career_salary = data_b.groupby('player_id')['salary'].mean()
    merged = data_a.merge(career_salary, left_on="_id",
                          right_on="player_id")
    merged['height'] = merged['height'].apply(_converting_machine)
    return merged


def _converting_machine(input_data):
    '''
    :param input_data: the input DataFrame that need to be transformed
    :return: float, the height of player in cm
    This function will help convert the player's height into cm.
    '''
    feet, inches = input_data.split("-")
    return 2.54 * (int(feet) * 12 + int(inches))
