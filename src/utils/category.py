import pandas as pd
import logging
import traceback
expense_seen = { 1 : 'groceries' , 2 : 'utilities' , 3 : 'entertainment'}


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/category.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

class CategoryManagement:

    def __init__(self):
        self.user_id = None
        self.df =  pd.read_csv('data/user.csv')

    def filter_by_category(self , user_id):
        try:
            global expense_seen
            self.user_id = user_id
            if user_id and  int(user_id) in self.df['user_id'].values:
                df_user = pd.read_csv(f'data/{self.user_id}.csv')
                cat = int(input('enter 1 for groceries  , 2 for utilities , 3 for entertainment : '))
                expense_type = expense_seen[cat]
                return df_user[df_user['expense_type'] == expense_type]
            else:
                return f'no data found of user_id {user_id}'
            
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}
        
if __name__ == '__main__':
    print('done')
        
