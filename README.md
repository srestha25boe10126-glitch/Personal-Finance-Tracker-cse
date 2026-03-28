# Personal-Finance-Tracker-cse
Project Overview
This is a simple command-line Student Expense Tracker built in Python. It allows students to add expenses in predefined categories, view all entries, get spending summaries, and find highest/lowest expenses—all using basic data structures like lists and dictionaries.
The app runs in a loop with a menu interface and handles input validation for amounts.
Features
•	Add expenses with amount and category (Food, Travel, Academics, Entertainment, Misc).
•	View all recorded expenses in a numbered list.
•	Calculate total spending and average expense.
•	Identify the highest and lowest expense amounts.
•	Invalid category defaults to "Misc"; non-numeric amounts show error messages.
Requirements
•	Python 3.6 or higher (uses built-in modules: sys, no external dependencies).
•	No additional libraries needed—pure standard library Python.
Setup Instructions
1.	Ensure Python is installed: Run python --version in your terminal. Download from python.org if needed.
2.	Create a new directory for the project: mkdir student-expense-tracker && cd student-expense-tracker.
3.	Save the provided code as expense_tracker.py in this directory.
Running the App
1.	Open a terminal in the project directory.
2.	Execute: python expense_tracker.py.
3.	Follow the on-screen menu: Select 1-5 to add/view expenses or exit.
4.	Data is stored in memory (resets on restart); add persistence like file saving for production.
Example first run output:
text
--- Welcome to the Student Expense Tracker ---
Usage Examples
•	Add Expense: Choose 1, enter amount (e.g., 10.50), category (e.g., Food).
•	View Expenses: Choose 2 to list all with indices.
•	Summary: Choose 3 for total/average after adding data.
•	Min/Max: Choose 4 to see extremes.
Troubleshooting
•	"Invalid input": Enter numeric amounts only.
•	No data errors: Add expenses first.
•	Customize categories by editing the categories list in code.
Future Improvements
Add file I/O for persistence, category editing, or reports export—great for academic extensions.

