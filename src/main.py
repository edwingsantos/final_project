# Run this file for full program
# import games - Solitaire, Freecell, Black Jack, Pyramid Solitaire
# from Lizzie's code import ..
# from Parkers's code import ..
# from Edwing's code import ..
# from Lucci's code import ..
# import tkinter

# def choices():
# Repeat until user chooses to Exit





#  Mainmenu
# Repeat until user chooses to Exit
# Display menu options with numbers:
# 1. Add Income
# 2. Add Expense
# 3. View Totals
# 4. Exit
# Prompt user to input a number (menu_option)

#   If user chooses 1:
#       take them to add incomefunciton

#   If user chooses 2:
#       take them to add expense

#   If user chooses 3:
#       take user to view totals

#   If user chooses 4:
#       take user to exit


































def options(root):
    def exit_program():
        sys.exit(0)
    # provide user with more options: add expense, add income, view total income or expenses in a specified time, set budget limits, compare budget to expenses, set savings goal, track progress towards savings goal, view budget as pie chart, view income/expenses as graph, log out
    instruction = tk.Label(root, text = "Welcome user. Choose an option below.")
        # EXPENSES:
            # run the income/expenses menu function
    income_expenses = tk.Button(root, text = "Manage Income/Expenses", command = menu)
        # SET LIMITS:
    limits = tk.Button(root, text = "Set Budget Limits", command = set_limits)
            # run the set budget limits function
        # COMPARE BUDGET/EXPENSES:
    compare = tk.Button(root, text = "Compare Budget to Expenses", command = compare_expenses)
            # run the compare budget and expenses function
        # SET SAVINGS GOAL:
    set_goal = tk.Button(root, text = "Set Savings Goal", command = app)
            # run the set savings goal function
        # TRACK PROGRESS TO GOAL:
    track_goal = tk.Button(root, text = "Track Progress to Goal", command = app)
            # run the track progress to savings goal function
        # VIEW PIE CHART:
    visualize = tk.Button(root, text = "Visualize Data", command = visualization_menu)
            # run the make pie chart function
        # QUIT:
    quit_main  = tk.Button(root, text = "Quit", command = exit_program)
    instruction.pack()
    income_expenses.pack()
    limits.pack()
    compare.pack()
    set_goal.pack()
    track_goal.pack()
    visualize.pack()
    quit_main.pack()


# main function:
def main():
    root = tk.Tk()
    root.title("personal Finance Main")
    root.minsize(300, 200)
    def remove_welcome():
        welcome.pack_forget()
        confirm_btn.pack_forget()
        options(root)
    # print a welcome and instructions for the user
    welcome = tk.Label(root, text = "Welcome user, to our personal finance program! In this program you have a wide variety of options of things to do! To budget, press the 'budgeting' button, to visualize your data, press the 'visualization' button, to do anything, press a button! Now go, and let your inner finance bro run wild!", wraplength = 300)
    confirm_btn = tk.Button(root, text = "OK")
    confirm_btn.config(command = remove_welcome)
    welcome.pack()
    confirm_btn.pack()
        # exit the loop
    root.mainloop()


main()