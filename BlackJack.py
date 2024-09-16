import random

while True:
    try:
        money = float(input("How much money do you have? $"))
        break
    except:
        continue
again = "y"


def cardLetter(sum_card_user):
    card_letter_list = ["10","Jack","Queen","King"]
    random_user = random.randint(1,10)
    if random_user == 1:
        card_letter = 'Ace'
        if sum_cards_user <= 10:
            random_user = 11
    elif random_user in range(2,10):
        card_letter = str(random_user)
    elif random_user == 10:
        card_letter = random.choice(card_letter_list)
    return card_letter,random_user



while again.lower() == "y":
    money_gamble = money + 1
    earned = 0
    sum_cards_user = 0
    random_dealer = 0
    random_user = 0
    if money != 0:
        while money_gamble > money:
            while True:
                try:
                    money_gamble = float(input("How much money do you want to gamble? $"))
                    break
                except:
                    continue
        money -= money_gamble
        first_card,random_user = cardLetter(sum_cards_user)
        sum_cards_user += random_user
        second_card,random_user = cardLetter(sum_cards_user)
        sum_cards_user += random_user
        print("Your first 2 cards are " + first_card + " and " + second_card + ("(" + str(sum_cards_user) + ")").rjust(10,' '))
        option = ""
        while sum_cards_user < 21 and option.lower() != "s":
            card_letter,random_user = cardLetter(sum_cards_user)
            option = ""
            while option.lower() != "h" and option.lower() != "s":
                option = input("Do you want to hit or stand (h/s)? ")
                print()
            if option.lower() == "h":
                sum_cards_user += random_user
                print("You got a " + card_letter + ("(" + str(sum_cards_user) + ")").rjust(30,' ') )

        print()
        random_dealer = random.randint(4,21)

        if sum_cards_user > random_dealer and sum_cards_user <= 21:
            print("You got " + str(sum_cards_user))
            print("The dealer got " + str(random_dealer))
            print("You won!")
            print()
            earned += money_gamble * 2
            money += earned
            print("Balance = $" + str(money) + "   + " + str(earned - money_gamble))
        if sum_cards_user < random_dealer or sum_cards_user > 21:
            print("You got " + str(sum_cards_user))
            if sum_cards_user < 21:
                print("The dealer got " + str(random_dealer))
            print("You lost")
            print()
            earned += money_gamble
            print("Balance = $" + str(money) + "   - " + str(earned))
        if sum_cards_user == random_dealer:
            print("You got " + str(sum_cards_user))
            print("The dealer got " + str(random_dealer))
            print("It's a draw!")
            print()
            earned += money_gamble
            money += earned
            print("Balance = $" + str(money) + "   + 0")

        again = input("Do you want to play again (y/n)? ")
    else:
        print("Go get some money! Your Broke.")
        break
