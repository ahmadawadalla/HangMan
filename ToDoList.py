"""
Requirements:
1. Add a Task: The user can add a new task to the to-do list.
2. View Tasks: The user can view all tasks. Completed tasks should be shown differently from incomplete ones.
3. Mark Task as Complete: The user can mark a specific task as complete.
4. Delete a Task: The user can delete a specific task from the list.
5. Persist Data: The tasks should be saved to a text file so that the list is not lost when the program exits.
"""

print("Here are the options: ")
print("(A) Add a Task"
      "\n(B) View Tasks"
      "\n(C) Mark Task as Complete"
      "\n(D) Remove Check Mark"
      "\n(E) Replace a Task"
      "\n(F) Delete a Task"
      "\n(G) Exit")

Tasks = open('Tasks.txt')

def read_file():
    Tasks = open('Tasks.txt', 'r')
    print("Here are the tasks: ")
    print()

    count = 0
    for i in Tasks.readlines():
        count += 1
        print(str(count) + '.', i.strip())

def replace_line():
    with open('Tasks.txt') as Tasks:
        replacing = Tasks.readlines()

    while True:
        replace = input("Which line do you want to replace: ")
        if replace.isdigit():
            replace = int(replace)
            if replace - 1 <= len(replacing):
                break
            else:
                print("Not in Range. Try Again.")
        else:
            print("Enter a number")

    replacing[replace - 1] = replacing[replace - 1].replace(replacing[replace - 1],'[ ] ' + input("What do you want to replace it with: ") + '\n')

    with open('Tasks.txt','w') as Tasks:
        for line in replacing:
            Tasks.write(line)

def delete_line():
    with open('Tasks.txt') as Tasks:
        deleting = Tasks.readlines()

    while True:
        delete = input("Which line do you want to delete: ")
        if delete.isdigit():
            delete = int(delete)
            if delete - 1 <= len(deleting):
                break
            else:
                print("Not in Range. Try Again.")
        else:
            print("Enter a number")

    del deleting[delete - 1]

    with open('Tasks.txt','w') as Tasks:
        for line in deleting:
            Tasks.write(line)

def completed_task():
    with open('Tasks.txt') as Tasks:
        lines = Tasks.readlines()

    while True:
        line_completed = input("Which Task did you complete: ")
        if line_completed.isdigit():
            line_completed = int(line_completed)
            if line_completed - 1 <= len(lines):
                break
            else:
                print("Not in Range. Try Again.")
        else:
            print("Enter a number")

    lines[line_completed - 1] = lines[line_completed - 1].strip().replace('[ ]','[' + u'\u2713' + ']') + '\n'

    with open('Tasks.txt','w') as Tasks:
        Tasks.writelines(lines)

def remove_check():
    with open('Tasks.txt') as Tasks:
        replacing = Tasks.readlines()

    while True:
        replace = input("Which line do you want to uncheck: ")
        if replace.isdigit():
            replace = int(replace)
            if replace - 1 <= len(replacing):
                break
            else:
                print("Not in Range. Try Again.")
        else:
            print("Enter a number")
    try:
        replacing[replace - 1] = replacing[replace - 1].replace('[' + u'\u2713' + '] ','[ ] ')
    except:
        print('That task is not finished.')

    with open('Tasks.txt','w') as Tasks:
        for line in replacing:
            Tasks.write(line)

# Code starts here
while True:
    print()
    option = input("Choose an option: ")

    # Add to file
    if option.lower() == 'a':
        Tasks = open('Tasks.txt', 'a')
        Tasks.write('[ ] ' + input("Enter the task description: ") + '\n')

    # Read the file
    elif option.lower() == 'b':
        read_file()

    # Put a check mark to indicate that it is complete
    elif option.lower() == 'c':
        completed_task()

    # Remove check mark
    elif option.lower() == 'd':
        remove_check()

    # Replace a task with a new task
    elif option.lower() == 'e':
        replace_line()

    # either delete a specific task, or all of them. If you want to delete all of them, make sure that the user is sure he wants to delete all the tasks
    elif option.lower() == 'f':
        delete_option = input("If you want to delete 1 line (Write 1) "
                              "\nIf you want to delete EVERYTHING (Write ALL) "
                              "\n--> ")
        if delete_option.lower() == '1':
            delete_line()
        elif delete_option.lower() == 'all':
            if input('Are you sure (y/n): ').lower() == 'y':
                Tasks = open('Tasks.txt','w')
                Tasks.write("")


    # end the code
    elif option.lower() == 'g':
        break

    else:
        continue

    Tasks.close()