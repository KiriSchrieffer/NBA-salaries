import Predictor as fun1
import pandas as pd


if __name__ == '__main__':
    data_a = pd.read_csv('players.csv')
    data_b = pd.read_csv('salaries_1985to2018.csv')
    data_c = pd.read_csv('salarycap.csv')
    fun1.salary_avg_points(data_a, data_b)
    fun1.avg_fg3_salary(data_a, data_b)
    fun1.salary_divide_salary_cap(data_a, data_b, data_c)
    fun1.salary_in_cap_3fg(data_a, data_b, data_c)
    fun1.prediction(data_a, data_b, data_c)


