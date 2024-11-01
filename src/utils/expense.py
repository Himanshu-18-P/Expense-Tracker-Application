import pandas as pd
import csv
from datetime import datetime
import logging
import traceback

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/expense.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

expense_seen = { 1 : 'groceries' , 2 : 'utilities' , 3 : 'entertainment'}

class ExpenseManagement:

    def __init__(self):
        self.new_user_header = ['date', 'expense_type', 'amount', 'note']
        self.user_id = None


    def load_data(self , path_of_csv ,user_id ):
        data = pd.read_csv(path_of_csv)
        self.user_id = user_id
        return data

    def check_user(self ,  user_id ,path = 'data/user.csv'):
        try:
            df = self.load_data(path , user_id)
            if user_id and  int(user_id) in df['user_id'].values:
                try:
                    data = self.load_data(f'data/{user_id}.csv' , user_id)
                    return True
                except FileNotFoundError:
                    return 'no such data exits'
            else:
                userid = input('please enter your phone number : ')
                if userid and  int(userid) in df['user_id'].values:
                    print(f'user_id already their ')
                    userid = input('please enter new phone number : ')
                print(f'your user_id is {userid}')
                name = input('please enter your name : ')
                new_user = {'user_id' : userid , 'name' : name }
                df = self.load_data('data/user.csv' , userid)
                df = df._append(new_user, ignore_index=True)
                df.to_csv('data/user.csv', index=False)
                with open(f'data/{userid}.csv', mode='w', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(self.new_user_header)
                return False
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}
        
    def add_record(self):
        try:
            global expense_seen
            print('-'*10)
            expense_input = int(input('enter 1 for groceries  , 2 for utilities , 3 for entertainment : '))
            expense_type = expense_seen[expense_input]
            try:
                amount = int(input('* enter your amount : '))
            except Exception as e:
                print('please enter valid number')
                amount = input('enter your amount : ')
            note_for_expense = input('* if you want to add any note : ')
            new_user = {'date' :datetime.now().date()  , 'expense_type' : expense_type , 'amount' : amount ,'note' : note_for_expense if note_for_expense else ''}
            df = pd.read_csv(f'data/{self.user_id}.csv')
            df = df._append(new_user, ignore_index=True)
            df.to_csv(f'data/{self.user_id}.csv', index=False)

            return "New record added succesfully"
        
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}
    
    def delete_data(self):
        try:
            print('-'*10)
            res = int(input('* to remove all data press 1\n* to remove of specific data by date press 2 : '))
            df = pd.read_csv(f'data/{self.user_id}.csv')
            print(df)
            if res and res == 1:
                df = df.drop(df.index) 
                df.to_csv(f'data/{self.user_id}.csv', index=False)
                return 'all data clear !!!!'
            else:
                your_year = input('* enter year(like 2014) : ')
                your_month = input('* enter month(like 01) : ')
                your_day = input('* end today date(like 09): ')
                print(df[df['date'] == f'{your_year}-{your_month}-{your_day}'].index)
                df = df.drop(df[df['date'] == f'{your_year}-{your_month}-{your_day}'].index)
                df.to_csv(f'data/{self.user_id}.csv', index=False)
                print(df)
                return 'give date data is clear' 
            
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}
    
    def modify_data(self):
        user_in = input('change date press 1 , change expense_type press 2 , change amount press 3')
        df = pd.read_csv(f'data/{self.user_id}.csv')
        if user_in and int(user_in) == 1:
            pass 
    
    
    
if __name__ == '__main__':
    print('done')








        