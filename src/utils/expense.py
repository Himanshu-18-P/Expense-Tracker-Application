import pandas as pd
import csv
from datetime import datetime

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
        df = self.load_data(path , user_id)
        if int(user_id) in df['user_id'].values:
            data = self.load_data(f'data/{user_id}.csv' , user_id)
            return data
        else:
            userid = input('please enter your phone number : ')
            print(f'your user_id is {userid}')
            name = input('please enter your name : ')
            new_user = {'user_id' : userid , 'name' : name }
            df = self.load_data('data/user.csv' , userid)
            df = df._append(new_user, ignore_index=True)
            df.to_csv('data/user.csv', index=False)
            with open(f'data/{userid}.csv', mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(self.new_user_header)
            return {'message' : "welcome to our app !!!"}
    
    def add_record(self):
        expense_input = int(input('enter 1 for groceries  , 2 for utilities , 3 for entertainment : '))
        expense_type = expense_seen[expense_input]
        try:
            amount = int(input('enter your amount : '))
        except Exception as e:
            print('please enter valid number')
            amount = input('enter your amount : ')
        note_for_expense = input('if you want to add any note : ')
        new_user = {'date' :datetime.now().date()  , 'expense_type' : expense_type , 'amount' : amount ,'note' : note_for_expense if note_for_expense else ''}
        df = pd.read_csv(f'data/{self.user_id}.csv')
        df = df._append(new_user, ignore_index=True)
        df.to_csv(f'data/{self.user_id}.csv', index=False)

        return {'message' : "New record added :)"}
    
if __name__ == '__main__':
    print('done')








        