# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Pavel,11.15.2020,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
# TODO: Add Code Here
try:
    f = open(objFile, 'r')
    for row in f:
        lstRow = row.split(',')
        dicRow = {'Task': lstRow[0], 'Priority': lstRow[1].strip()}
        lstTable.append(dicRow)
    f.close()
except:
    print('No data exist')
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        # TODO: Add Code Here
        for i in lstTable:
            print(i)
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        # TODO: Add Code Here
        task = input('What is your task: ')
        # Check if task is already in list and if it is then message user:
        lstTasks = []
        for i in lstTable:
            lstTasks.append(i['Task'].lower())
        if task.lower().strip() in lstTasks:
            print('That task is already in the list. Try again or make another selection.')
            continue
        priority = input('List priority: ')
        newRow = {'Task': task.strip(), 'Priority': priority.strip()}
        lstTable.append(newRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        # TODO: Add Code Here
        delete = input('What do you want to delete: ')
        lstTasks = []
        for i in lstTable:
            lstTasks.append(i['Task'].lower())
        if delete.lower().strip() not in lstTasks:
            print('This task is not in the list. Try again or make another selection')
            continue
        for i in lstTable:
            if i['Task'].lower() == delete.lower().strip():
                lstTable.remove(i)
                break
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        # TODO: Add Code Here
        f = open(objFile, 'w')
        for i in lstTable:
            f.write(i['Task'] + ',' + i['Priority'] + '\n')
        f.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        print('You have exited')
        break  # and Exit the program
