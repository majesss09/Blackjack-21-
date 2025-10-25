import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play == "y":
    print("\n" *20, art.logo)
    player_hand = [random.choice(cards),random.choice(cards)]
    dealer_hand = [random.choice(cards),random.choice(cards)]
    player_score = sum(player_hand)
    print(f"    Your cards: {player_hand}, current score = {[player_score]}")
    print(f"    Computer's first hand: {dealer_hand}")

    if sum(player_hand) != 21:
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        while player_score < 21 and draw == "y":
            drawn_card = random.choice(cards)
            if drawn_card == 11 and sum(player_hand) > 11:
                player_hand.append(1)
            else:
                player_hand.append(drawn_card)
            player_score = sum(player_hand)
            print(f"    Your cards: {player_hand}, current score = {player_score}")
            print(f"    Computer's first hand: {dealer_hand[0]}")
            if player_score < 21:
                draw = input("Type 'y' to get another card, type 'n' to pass: ")

    player_score = sum(player_hand)
    dealer_score = sum(dealer_hand)

    while dealer_score <= 16:
        drawn_card = random.choice(cards)
        if drawn_card == 11 and sum(dealer_hand) > 11:
            dealer_hand.append(1)
        else:
            dealer_hand.append(drawn_card)
        dealer_score = sum(dealer_hand)
    print(f"   Your final hand: {player_hand}, final score: {player_score}")
    print(f"   Computer's final hand: {dealer_hand}, final score: {dealer_score}")

    if player_score == dealer_score:
        print("Draw 🙃")
    else:
        if player_score == 21:
            print("Win with a Blackjack 😎")
        if dealer_score > 21:
            if player_score <= 21 and player_score != 21:
                print("Opponent went over. You win 😁")
            else:
                print("Draw 🙃")
        else:
            if player_score <= 21:
                if player_score > dealer_score:
                    print("You win 😃")
                elif dealer_score > player_score:
                    print("You lose 😤")
                else:
                    print("Draw 🙃")
            else:
                print("You went over. You lose 😭")
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")