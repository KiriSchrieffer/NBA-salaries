import q4 as q4


def main():
    AST = float(input("What is your assist per game? "))
    PTS = float(input("What is your points per game? "))
    FG3 = float(input("What is your 3-point field goal percentage? "))
    print("Your expected salary is $" + str(
        (q4.predict_salary_usecap([[AST, PTS, FG3]]))[0]) + "!")


if __name__ == '__main__':
    main()
