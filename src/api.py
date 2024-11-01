from src.utils.expense import *
from src.utils.category import *
from src.utils.expensetracker import *

class ProcessAPI:

    def __init__(self):
        self.expense = ExpenseManagement()
        self.cat_filter = CategoryManagement()
        self.report = GenrateReport()


if __name__ == '__main__':
    print('done')