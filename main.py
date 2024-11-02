import pandas as pd 
from src.api import *
import logging
import traceback

user_path = 'data/user.csv'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/main.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)



def is_user_new(res):
    if res == True:
        change = int(input('* 1 for add record \n* 2 for remove record \n* 3 for modify record : '))
        if change == 1:
            res = process.expense.add_record()
        elif change == 2:
            res = process.expense.delete_data()   
        else:   
            res = process.expense.modify_data()        
        return  res 
    else:
        change = input('* press 1 to add record and enter to skip : ')
        if int(change) == 1:
            res = process.expense.add_record()
        else:
            res = 'thanks for visiting !!'
        return res 

def check_field(user_id , is_user ):
        if is_user:
            check_field = int(input('''* 1 for Expense(add , delete , modification)  
                                    \n*2 for Category Management(filter data based on Category)
                                    \n* 3 for Report Generation ((daily, weekly, monthly) and per category) : '''))
            if check_field == 1:
                res = is_user_new(is_user)
            elif check_field == 2:
                print('-'*10)
                res = process.cat_filter.filter_by_category(user_id)
                print(res)
            else:
                process.report.set_df(user_id)
                specific_time = int(input('''* 1 for today report
                                    \n*2 for today this week report
                                    \n* 3 for today this month report: ''')) 
                if specific_time == 1:
                    res = process.report.today_report()
                    print(res)
                elif specific_time == 2:
                    res = process.report.weekly_report()
                    print(res)
                else:
                    res = process.report.monthly_report()
                    print(res)
        else:
            res = is_user_new(is_user)
        return res 
                



def main():
    try:
        print('hello welcome to our app :)')
        user_id = input('* if you have userid please enter otherwise just press enter : ')
        is_user = process.expense.check_user(user_id)
        print(is_user)
        print('-'*10) 
        res = check_field(user_id , is_user)
        print('-'*10)
        return res
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.error(traceback.format_exc())
        return {"error": "An internal error occurred. Please try again later."}

if __name__ == '__main__':
    process = ProcessAPI()
    main()
    # df = pd.read_csv('data/user.csv')
    # print(df[df['user_id'] == '123'].index)
    # print(type(df['user_id'].values[0]))
    # print('123' in df['user_id'].values)