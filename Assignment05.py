# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# BSpadavecchia,02-13-2022,Added code to complete assignment 5
# BSpadavecchia,02-14-2022,Revised code on assignment 5
# BSpadavecchia,02-15-2022,Added try except on assignment 5
# BSpadavecchia,02-16-2022,Revised code on assignment 5
# BSpadavecchia,02-17-2022,Revised code on "Add a new item"
# BSpadavecchia,02-18-2022,Revised code on "Remove an existing item"
# BSpadavecchia,02-19-2022,Revised code on "Save Data to File
# ------------------------------------------------------------------------ #

# -- Data -- #
# Step 1 - declare variables and constants
objFile = []
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option select
strFileName = "ToDoList.txt"

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
#  The try-except is checking to see if the "ToDoList.txt" file has anything in it to load
try:
    print("What task do you need to do?")
    print("Here are your current tasks:")
    objFile = open(strFileName, "r")
    for row in objFile:
        strData = row.split(",")
        dicRow = {"task": strData[0].strip(), "priority": strData[1].strip()}
        print(dicRow)
        lstTable.append(dicRow)
    objFile.close()
    input("Press enter to continue")
except:
    if len(strFileName) < 1:
        print("Your ToDo List is empty")

# TODO: Add Code Here (possible revision on print format)
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
    if (strChoice.strip() == '1'):
        print("**********Here is your current ToDo list:************\n")
        for row in lstTable:
            print("Task:", row['task'], "|", "Priority:", row['priority'])
        else:
            if len(lstTable) == 0:
                print("You have nothing in your ToDo list")
        continue

        # TODO: Add Code Here
        # Step 3 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("Please enter a new task:  ").strip()
        strPriority = input("Please enter a priority:  ").strip()
        print("************************************************") #  adding a new line for looks
        print("**********Here is your current ToDo list:************\n")
        dicRow = {"task": strTask, "priority": strPriority}
        lstTable.append(dicRow)
        for row in lstTable:
            print("Task:", row['task'], "|", "Priority:", row['priority'])

        continue
        # Step 4 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        print("Here is your current ToDo List:\n")
        for row in lstTable:
            print("Task:", row['task'], "|", "Priority:", row['priority'])
        strKeytoRemove = input("\nWhat task do you want to delete?  ")
        for row in lstTable:
            if row['task'].lower() == strKeytoRemove.lower():
                lstTable.remove(row)
                print("Task: " + strKeytoRemove + " was removed from list\n")
                print("Here is your current list")
                for row in lstTable:
                    print("Task:", row['task'], "|", "Priority:", row['priority'])
            else:
                print("That task does not exit")
        print("*****" * 6)

     # TODO: Add Code Here (Would like more Error Handling)
        continue
    # Step 5 - Save tasks to the ToDoList.txt file

    elif (strChoice == '4'):
        # Step 5a - Show the current items in the table
        print("*****" *6)
        print("Here is your current list")
        for row in lstTable:
            print("Task:", row['task'], "|", "Priority:", row['priority'])
        print("*****" * 6)

        # Step 5b - Ask if they want save that data
        if ("y" == str(input("Save this data to file? (y/n) - ")).strip().lower()):
            objFile = open(strFileName, "w")
            for dicRow in lstTable:
                objFile.write(dicRow["task"] + "," + dicRow["priority"] + "\n")
            objFile.close()
            input("Data saved to file! Press the [Enter] key to return to menu.")
        else:
            input("New data was NOT Saved.  Please press [Enter] to return to Menu.")
            continue

        # TODO: Add Code Here
        continue
    # Step 6 - Exit program
    elif (strChoice.strip() == '5'):
        # TODO: Add Code Here
        break  # and Exit the program

    else:
        print("\n Please choose a menu option [1-5]\n")
