import random

lost = 0
won = 0
draw = 0

again = 'y'
while again.lower() == 'y':
    row1 = (["_","_","_"])
    row2 = (["_","_","_"])
    row3 = (["_","_","_"])

    user_xo = random.randint(1,2)
    col = ['A','B','C']
    row = ['1','2','3']

    def machine(rep):
        machine_input = 'X' # initializing

        while machine_input != '_':
            machine_col = random.choice(col)
            machine_row = random.randint(1,3)
            index = ord(machine_col) - ord('A')
            if machine_row == 1:
                machine_input = row1[index]

            elif machine_row == 2:
                machine_input = row2[index]

            elif machine_row == 3:
                machine_input = row3[index]

        if machine_row == 1:
            row1[index] = row1[index].replace('_',rep)
            return row1,row2,row3
        elif machine_row == 2:
            row2[index] = row2[index].replace('_',rep)
            return row1,row2,row3
        elif machine_row == 3:
            row3[index] = row3[index].replace('_',rep)
            return row1,row2,row3

    def user(rep):
        user_input = 'X'
        while user_input != '_':

            user_row = 0
            while user_row not in row:
                user_row = input("Which row (1,2,3): ")
            user_col = 0
            while user_col not in col:
                user_col = input("Which column (A,B,C): ").upper()

            if user_row == '1':
                user_input = row1[ord(user_col) - ord('A')]
            elif user_row == '2':
                user_input = row2[ord(user_col) - ord('A')]
            elif user_row == '3':
                user_input = row3[ord(user_col) - ord('A')]

        if user_row == '1':
            row1[ord(user_col) - ord('A')] = row1[ord(user_col) - ord('A')].replace('_',rep)
            return row1,row2,row3
        elif user_row == '2':
            row2[ord(user_col) - ord('A')] = row2[ord(user_col) - ord('A')].replace('_',rep)
            return row1,row2,row3
        elif user_row == '3':
            row3[ord(user_col) - ord('A')] = row3[ord(user_col) - ord('A')].replace('_',rep)
            return row1,row2,row3

    if user_xo == 1:
        print()
        print(">>> You are X <<<")
        print()
        print("    A   B   C")
        print("1 ["," | ".join(row1),"]")
        print("2 ["," | ".join(row2),"]")
        print("3 ["," | ".join(row3),"]")
        print()
        user('X')
        while '_' in row1 or '_' in row2 or '_' in row3:
            machine('O')
            print()
            condition = False
            # Conditions for O
            if 'O' in row1[0] and 'O' in row1[1] and 'O' in row1[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row2[0] and 'O' in row2[1] and 'O' in row2[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row3[0] and 'O' in row3[1] and 'O' in row3[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row1[0] and 'O' in row2[0] and 'O' in row3[0]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row1[1] and 'O' in row2[1] and 'O' in row3[1]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row1[2] and 'O' in row2[2] and 'O' in row3[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row1[0] and 'O' in row2[1] and 'O' in row3[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'O' in row1[2] and 'O' in row2[1] and 'O' in row3[0]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break

            print("    A   B   C")
            print("1 ["," | ".join(row1),"]")
            print("2 ["," | ".join(row2),"]")
            print("3 ["," | ".join(row3),"]")
            print()

            user('X')
            print()
            # Conditions for X
            if 'X' in row1[0] and 'X' in row1[1] and 'X' in row1[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row2[0] and 'X' in row2[1] and 'X' in row2[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row3[0] and 'X' in row3[1] and 'X' in row3[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row1[0] and 'X' in row2[0] and 'X' in row3[0]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row1[1] and 'X' in row2[1] and 'X' in row3[1]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row1[2] and 'X' in row2[2] and 'X' in row3[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row1[0] and 'X' in row2[1] and 'X' in row3[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'X' in row1[2] and 'X' in row2[1] and 'X' in row3[0]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break

    else:
        print()
        print(">>> You are O <<<")
        print()
        while '_' in row1 or '_' in row2 or '_' in row3:
            machine('X')

            print("    A   B   C")
            print("1 ["," | ".join(row1),"]")
            print("2 ["," | ".join(row2),"]")
            print("3 ["," | ".join(row3),"]")
            print()
            condition = True
            # Conditions for X
            if 'X' in row1[0] and 'X' in row1[1] and 'X' in row1[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row2[0] and 'X' in row2[1] and 'X' in row2[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row3[0] and 'X' in row3[1] and 'X' in row3[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row1[0] and 'X' in row2[0] and 'X' in row3[0]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row1[1] and 'X' in row2[1] and 'X' in row3[1]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row1[2] and 'X' in row2[2] and 'X' in row3[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row1[0] and 'X' in row2[1] and 'X' in row3[2]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break
            elif 'X' in row1[2] and 'X' in row2[1] and 'X' in row3[0]:
                condition = True
                print(">>>You Lose !!!<<<")
                lost += 1
                break

            if '_' in row1 or '_' in row2 or '_' in row3:
                user('O')
            print()

            # Conditions for O
            if 'O' in row1[0] and 'O' in row1[1] and 'O' in row1[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row2[0] and 'O' in row2[1] and 'O' in row2[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row3[0] and 'O' in row3[1] and 'O' in row3[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row1[0] and 'O' in row2[0] and 'O' in row3[0]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row1[1] and 'O' in row2[1] and 'O' in row3[1]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row1[2] and 'O' in row2[2] and 'O' in row3[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row1[0] and 'O' in row2[1] and 'O' in row3[2]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break
            elif 'O' in row1[2] and 'O' in row2[1] and 'O' in row3[0]:
                condition = True
                print(">>>You Win !!!<<<")
                won += 1
                break

    if condition == False:
        print(">>>Draw !!!<<<")

    print()
    print("    A   B   C")
    print("1 ["," | ".join(row1),"]")
    print("2 ["," | ".join(row2),"]")
    print("3 ["," | ".join(row3),"]")

    again = input("Do you want to play again (y/n)? ")

print()
print("Wins:",won)
print("Losses:",lost)
if draw > 0:
    print("Draws:",draw)