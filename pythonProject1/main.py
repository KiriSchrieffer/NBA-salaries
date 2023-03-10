import Predictor as fun1
import pandas as pd


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    data_a = pd.read_csv('players.csv')
    data_b = pd.read_csv('salaries_1985to2018.csv')
    data_c = pd.read_csv('salarycap.csv')
    fun1.salary_avg_points(data_a, data_b)
    fun1.avg_fg3_salary(data_a, data_b)
    fun1.salary_divide_salary_cap(data_a, data_b, data_c)
    fun1.salary_in_cap_3fg(data_a, data_b, data_c)
    fun1.prediction(data_a, data_b, data_c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
