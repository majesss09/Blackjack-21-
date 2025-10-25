# 🃏 Blackjack – Python Console Game

A fun and interactive **Blackjack (21)** game built in Python.  
This project lets you play against a computer dealer, draw cards, and test your luck while learning about loops, functions, and conditional logic.

---

## 🧩 About the Game
Blackjack is a popular card game where the goal is to have a hand value closer to **21** than the dealer’s — without going over.

### 🎮 How It Works
- You start with **two random cards**.  
- You can **draw additional cards** (`y`) or **pass** (`n`).  
- The computer (dealer) draws cards until its total is **above 16**.  
- The program compares scores and declares the result.

---

## 🖼️ ASCII Art Logo
Displayed at the start of the game using the `art` module:
.------. _ _ _ _ _
|A_ _ |. | | | | | | () | |
|( / ).-----. | |__ | | __ _ | | ___ __ _ __| | __
| \ /|K /\ | | ' | |/ |/ __| |/ / |/ _ |/ __| |/ /
| / | / \ | | |) | | (| | (| <| | (| | (| <
-----| \ / | |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\ | \/ K| _/ | ------' |/


---

## 💻 Code Overview
```python
import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
while play == "y":
    print("\n" * 20, art.logo)
    player_hand = [random.choice(cards), random.choice(cards)]
    dealer_hand = [random.choice(cards), random.choice(cards)]
    player_score = sum(player_hand)
    print(f"    Your cards: {player_hand}, current score = {player_score}")
    print(f"    Computer's first hand: {dealer_hand[0]}")

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
    elif player_score == 21:
        print("Win with a Blackjack 😎")
    elif dealer_score > 21:
        if player_score <= 21:
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
```
---

## 🧮 Example Gameplay


Do you want to play a game of Blackjack? Type 'y' or 'n': y


Your cards: [10, 8], current score = 18


Computer's first hand: 7


Type 'y' to get another card, type 'n' to pass: n



Your final hand: [10, 8], final score: 18


Computer's final hand: [7, 9, 5], final score: 21


You lose 😤


