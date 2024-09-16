import random

again = 'y'
while again.lower() == 'y':
    fruits = ["apple","banana", "strawberry","raspberry","blueberry","orange","carrot","pear","mango","avocado","guava","cranberry","nectarine","plum","pomegranate","peach",
              "blackberry","grape","boysenberry","watermelon","cantaloupe","date","lemon","lychee","fig","lime","pineapple","olive","apricot","celery","cucumber"]

    school = ["computer","science","physics","math","calculus","pencil","pen","notes","notebook","university","eraser","ruler","paper", "algebra","trigonometry","backpack",
              "calculator","textbook","chalk","board","marker"]

    combined_list = []
    combined_list.extend(fruits)
    combined_list.extend(school)

    random_word = random.choice(combined_list) # chooses a random word from the list

    if random_word in fruits:
        print("Hint: \"It's a fruit\"")
    elif random_word in school:
        print("Hint: \"It's school related\"")

    letters = []
    i = 0
    while True:
        if i < len(random_word):
            letters.append(random_word[i])
            i += 1
        else:
            break

    length_letters = []
    wrong = 0

    spaces = [] # The amount of blank spaces for the word
    k = 0
    while k < len(letters):
        spaces.append('_')
        k += 1

    print("[" + " ".join(spaces) + "]")
    while len(length_letters) != len(letters):
        if wrong < 10:
            user_guess = input("guess a letter (-1 to quit): ")
            print()
            if user_guess == '-1':
                break
            if user_guess.lower() in letters:
                print("you got it!")
                j = 0
                while j < len(letters):
                    if user_guess in letters[j]:
                        letters[j] = letters[j].replace(user_guess, '-1')
                        spaces[j] = spaces[j].replace(spaces[j],user_guess)
                        length_letters.append(j)
                    j += 1
            else:
                wrong += 1
                print("You have " + str(wrong) + " / 10 wrong")
            print("[" + " ".join(spaces) + "]")
        else:
            print("You got 10 wrong, good game")
            break
    if len(length_letters) == len(letters):
        print("Good Job, You won!!")
    print("The correct answer was " + random_word)
    print()

    again = input("Do you want to play again (y/n)? ")
