import pandas as pd 
from src.api import *

user_path = 'data/user.csv'
def main():
    print('hello welcome to our app :)')
    user_id = input('if you have userid please enter otherwise just press enter : ')
    process.expense.check_user(user_id)
    add_record = int(input('if you want to add record 1 else 0 : '))
    if add_record == 1:
        res = process.expense.add_record()
        return res
    else:
        return 'thanks for visiting' 

if __name__ == '__main__':
    process = ProcessAPI()
    print(main())
    # df = pd.read_csv('data/user.csv')
    # print(df[df['user_id'] == '123'].index)
    # print(type(df['user_id'].values[0]))
    # print('123' in df['user_id'].values)