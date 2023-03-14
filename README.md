# NBA salaries predictor
## For Question 1 and 2
You should download all the files in the 'NBASalaryPredictrorQ1Q2', and you should make sure you have installed altair and pandas libraries.
Next, you should put all the files under one file folder, and then you can run 'main.py' to get the picture you want.
## For Question 4
Download the folder 'NBASalaryPredictorQ4'.
Download Microsoft Excel App.
Firstly, run 'q4.py' to train the model using 'salaries_1985to2018.csv', 'salary_cap.csv' and 'players.csv'.
Then run 'main.py'. It will guide you to input data and make prediction.
If you want to test the model, run 'q4_test.py'. It uses data from 'test_points_2023.csv' and 'test_salary_2023.csv' to test the accuracy of the prediction program.
The test gives you R-squared values and the percentage of relative error less than 50% of training the model WITH or WITHOUT using salary cap.
These two test files are provided in the folder, but if you want to get them by yourself, run 'get_test_points_2023.py' and 'get_test_salary_2023.py'.
'get_test_points_2023.py' crawls data from https://www.basketball-reference.com/leagues/NBA_2023_totals.html
'get_test_salary_2023.py' crawls data from http://www.espn.com/nba/salaries
They save the data in csv files, encoding ANSI.
You have to open the csv files with Excel and save them as encoding UTF-8 to make them readable for 'q4_test.py'
