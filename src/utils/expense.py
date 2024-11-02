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
            print('-' * 10)
            res = int(input('* To remove all data press 1\n* To remove specific data by date press 2: '))
            df = pd.read_csv(f'data/{self.user_id}.csv')
            if res == 1:
                df = df.drop(df.index)
                df.to_csv(f'data/{self.user_id}.csv', index=False)
                return 'All data cleared!'
            elif res == 2:
                date_str = input('Enter the date of the record you want to delete (YYYY-MM-DD): ')
                try:
                    date_to_delete = datetime.strptime(date_str, '%Y-%m-%d').date()
                except ValueError:
                    print('Invalid date format. Please use YYYY-MM-DD.')
                    return
                df['date'] = pd.to_datetime(df['date']).dt.date
                indices = df[df['date'] == date_to_delete].index
                if not indices.empty:
                    df = df.drop(indices)
                    df.to_csv(f'data/{self.user_id}.csv', index=False)
                    return f'Data for {date_to_delete} has been deleted.'
                else:
                    return 'No data found for the specified date.'
            else:
                return 'Invalid option selected.'

        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}

    def modify_data(self):
        try:
            df = pd.read_csv(f'data/{self.user_id}.csv')
            if df.empty:
                print('No records to modify.')
                return
            df['date'] = pd.to_datetime(df['date']).dt.date

            print(df)
            index_to_modify = int(input('Enter the index of the record you want to modify: '))
            if index_to_modify not in df.index:
                print('Invalid index.')
                return

            print('What do you want to modify?')
            print('1. Date')
            print('2. Expense Type')
            print('3. Amount')
            print('4. Note')
            choice = int(input('Enter your choice: '))

            if choice == 1:
                new_date_str = input('Enter new date (YYYY-MM-DD): ')
                try:
                    new_date = datetime.strptime(new_date_str, '%Y-%m-%d').date()
                    df.at[index_to_modify, 'date'] = new_date
                except ValueError:
                    print('Invalid date format.')
                    return
            elif choice == 2:
                print('Select new expense type:')
                for key, value in expense_seen.items():
                    print(f'{key}: {value}')
                new_expense_input = int(input('Enter your choice: '))
                new_expense_type = expense_seen.get(new_expense_input, None)
                if new_expense_type:
                    df.at[index_to_modify, 'expense_type'] = new_expense_type
                else:
                    print('Invalid expense type selected.')
                    return
            elif choice == 3:
                new_amount = float(input('Enter new amount: '))
                df.at[index_to_modify, 'amount'] = new_amount
            elif choice == 4:
                new_note = input('Enter new note: ')
                df.at[index_to_modify, 'note'] = new_note
            else:
                print('Invalid choice.')
                return

            df.to_csv(f'data/{self.user_id}.csv', index=False)
            print('Record updated successfully.')
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            print("An internal error occurred. Please try again later.")
    
if __name__ == '__main__':
    print('done')








        