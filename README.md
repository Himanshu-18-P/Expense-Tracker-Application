# Expense-Tracker-Application
this is expense tracker python application 

The Expense Management System is a command-line application that allows users to manage their expenses efficiently. Users can add, modify, delete, and categorize their expenses, as well as generate reports based on specified time intervals (daily, weekly, monthly) and categories.

Features
User Management

Checks if a user already exists.
Adds new users with unique user IDs.
Expense Management

Add new expense records.
Delete expense records (all or by specific date).
Modify existing expense records.
Category Management

Filter expense records based on categories (e.g., groceries, utilities, entertainment).
Report Generation

Generate daily, weekly, and monthly expense reports.
Generate reports filtered by specific categories.
Directory Structure
bash
Copy code
├── data/
│   ├── user.csv              # Stores user information (user_id, name)
│   └── {user_id}.csv         # Individual user expense files
├── log/
│   ├── expense.log           # Log file for expense operations
│   └── main.log              # Log file for main operations
│   ├── category.log          # Log file for category operations
│   └── expensetracker.log    # Log file for expensetracker operations
├── src/
│   └── api.py                # Contains the main API classes and methods
│   └── utils/                # Contains the  classes and methods for all methods
├── main.py                   # Entry point for the application
├── requirements.txt          # List of Python dependencies
├── README.md                 # Project documentation
└── .gitignore                # Ignored files and directories

Installation
Clone the repository and navigate to the project directory.

Install the required packages listed in requirements.txt:

bash
Copy code
pip install -r requirements.txt
Ensure the data and log directories exist:

bash
Copy code
mkdir -p data log
Dependencies
The application depends on the following libraries:

pandas: Used for data manipulation and management.
Additional dependencies can be specified in requirements.txt.

Usage
Run the application using:

bash
Copy code
python main.py
Main Workflow
User Identification

If the user ID exists, the system loads the user data; otherwise, it prompts for registration.
Expense Options

Add, delete, or modify expense records.
Filter expenses by category or generate reports.
Options Available
1. Expense Operations
Add Record: Adds a new expense.
Delete Record: Deletes all expenses or only those for a specific date.
Modify Record: Modifies an existing expense record.
2. Category Management
Filters expenses based on categories such as groceries, utilities, or entertainment.
3. Report Generation
Daily Report: Shows expenses for the current day.
Weekly Report: Shows expenses for the past 7 days.
Monthly Report: Shows expenses for the current month.
Sample Prompts
When running the program, you'll encounter prompts like:

Choose Operation

1 for adding an expense
2 for deleting an expense
3 for modifying an expense
Report Options

1 for today's report
2 for weekly report
3 for monthly report
Logging
The application logs its operations in the following files:

log/expense.log: Logs activities related to expense management.
log/main.log: Logs main application operations, including error handling.
Logs are helpful for debugging and keeping track of user interactions.

Files
main.py: The main application file that initializes the application and processes user inputs.
api.py: Contains the ExpenseManagement class with methods for expense management, category filtering, and report generation.
user.csv: Stores user data (user_id, name).
{user_id}.csv: Stores each user's expenses (date, expense type, amount, note).
Example Usage
arduino
Copy code
hello welcome to our app :)
* if you have userid please enter otherwise just press enter :
Based on your responses, you can perform actions such as adding a record, generating a report, or filtering by category.

Error Handling
The application is designed to handle errors gracefully:

Exceptions are logged in the respective log files.
If an error occurs, the application displays an error message and logs the traceback for debugging.
Notes
Ensure the data directory exists and contains the user.csv file for user management.
Expense categories are predefined in expense_seen as:
1: Groceries
2: Utilities
3: Entertainment