import pandas as pd
from datetime import datetime , timedelta
import logging
import traceback

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')

file_handler = logging.FileHandler('log/expensetracker.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

expense_seen = { 1 : 'groceries' , 2 : 'utilities' , 3 : 'entertainment'}

class GenrateReport:

    def __init__(self):
        self.today_date = datetime.now().date()
        self.df = None

    def set_df(self, userid):
        self.df = pd.read_csv(f'data/{userid}.csv')
        self.df['date'] = pd.to_datetime(self.df['date'], format='%Y-%m-%d').dt.date

    def today_report(self):
        try:
            return self.df[self.df['date'] == self.today_date]
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}

    def weekly_report(self):
        try:
            week_ago = self.today_date - timedelta(days=7)
            mask = (self.df['date'] >= week_ago) & (self.df['date'] <= self.today_date)
            return self.df[mask]
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}

    def monthly_report(self):
        try:
            first_day_of_month = self.today_date.replace(day=1)
            mask = (self.df['date'] >= first_day_of_month) & (self.df['date'] <= self.today_date)
            return self.df[mask]
        except Exception as e:
            logger.error(f"Error: {e}")
            logger.error(traceback.format_exc())
            return {"error": "An internal error occurred. Please try again later."}

if __name__ == '__main__':
    print('done')
