import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

cards = [
''' _____
 |A  | 
 |(`)| 
 |_\_|''',
 
 ''' _____
 |2  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |3  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |4  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |5  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |6  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |7  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |8  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |9  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |10  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |J  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |Q  | 
 |(`)| 
 |_\_|''',

 ''' _____
 |K  | 
 |(`)| 
 |_\_|''',
 ]

victory = '''____   ____.__        __                       ._.
\   \ /   /|__| _____/  |_  ___________ ___.__.| |
 \   Y   / |  |/ ___\   __\/  _ \_  __ <   |  || |
  \     /  |  \  \___|  | (  <_> )  | \/\___  | \|
   \___/   |__|\___  >__|  \____/|__|   / ____| __
                   \/                   \/      \/
                   '''


defeat = '''________          _____              __  ._.
\______ \   _____/ ____\____ _____ _/  |_| |
 |    |  \_/ __ \   __\/ __ \\__  \\   __\ |
 |    `   \  ___/|  | \  ___/ / __ \|  |  \|
/_______  /\___  >__|  \___  >____  /__|  __
        \/     \/          \/     \/      \/
        '''

draw = ''' ________                      ._.
\______ \____________ __  _  _| |
 |    |  \_  __ \__  \\ \/ \/ / |
 |    `   \  | \// __ \\     / \|
/_______  /__|  (____  /\/\_/  __
        \/           \/        \/

        '''



print (logo)
print ("Welcome to blackjack! The rules are simple. Try to beat the computer by accumulating a hand with the highest sum while still keeping it below 21! If the computer gets a higher sum than you do or you hit 21 you lose!")

computer_stops = False

AI_options = [1,2]

card = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]

user_card_1 = random.choice (card)
user_card_2 = random.choice (card)
computer_card_1 = random.choice (card)


if computer_card_1 == "J" or computer_card_1 == "Q" or computer_card_1 == "K":
    computer_card_1_value = (10)
elif computer_card_1 == "A":
    computer_card_1_value = (11)
else:
    computer_card_1_value = (computer_card_1)

computer_cards =  [computer_card_1]

computer_cards_value = [computer_card_1_value]

computer_cards_string = str (computer_cards [0])

print (f"The computer's current hand is: {computer_cards_string}")

continue_game = True

if user_card_1 == "J" or user_card_1 == "Q" or user_card_1 == "K":
    user_card_1_value = 10
elif user_card_1 == "A":
    user_card_1_value = 11
else:
    user_card_1_value = user_card_1

if user_card_2 == "J" or user_card_2 == "Q" or user_card_2 == "K":
    user_card_2_value = 10
elif user_card_2 == "A":
    user_card_2_value = 11
else:
    user_card_2_value = user_card_2

current_hand_user = str (user_card_1) + ", " + str (user_card_2)
current_hand_numeric_user = [user_card_1_value, user_card_2_value]

sum_of_user_hand = sum (current_hand_numeric_user)

sum_of_computer_hand = sum (computer_cards_value)

print (f"Your current hand is: {current_hand_user}")
user_threshold =  (sum_of_user_hand)
computer_threshold =  (sum_of_computer_hand)

i = 1

while continue_game == True:

    would_you_like_to_continue = input ("\nHit or Hold? Type 'Hit' to hit or 'Hold' to stop: ").lower()

    

    if would_you_like_to_continue == "hold" and user_threshold != 21 and computer_threshold != 21:
        comp = 1

        while comp == 1 and computer_threshold <= 21:
            computer_card_generated = random.choice (card)
            if computer_card_generated == "J" or computer_card_generated == "Q" or computer_card_generated == "K":
                computer_card_generated_value =  (10)
            elif computer_card_generated == "A":
                computer_card_generated_value =  (11)
            else:
                computer_card_generated_value = (computer_card_generated)

            print (f"The computer has drawn a {computer_card_generated}!")
            print (cards [card.index (computer_card_generated)])
            
            computer_cards.append(computer_card_generated)

            computer_cards_value.append (computer_card_generated_value)

            for index in range (i, len (computer_cards)):
                computer_cards_string += ", " + str (computer_cards [index])
            
            i += 1

            computer_threshold = sum(computer_cards_value)
            if computer_threshold > 21 and computer_cards_value.count (11) >= 1:
                computer_cards_value.remove (11)
                computer_cards_value.append (1)
                computer_threshold = sum (computer_cards_value)

            comp = random.choice (AI_options)
        
        continue_game = False

    elif would_you_like_to_continue == "hit" and user_threshold != 21 and computer_threshold != 21:    
        user_card_generated = random.choice (card)
        if user_card_generated == "J" or user_card_generated == "Q" or user_card_generated == "K":
            user_card_generated_value = (10)
        elif user_card_generated == "A":
            user_card_generated_value =  (11)
        else:
            user_card_generated_value = (user_card_generated)

        current_hand_user += ", " + str (user_card_generated)

        current_hand_numeric_user += [user_card_generated_value]

        sum_of_hand = sum (current_hand_numeric_user)
        
        print (f"You have drawn a {user_card_generated}!")
        print (cards [card.index (user_card_generated)])


        print (f"Your current hand is: {current_hand_user}\n")

        user_threshold = sum(current_hand_numeric_user)
        if user_threshold > 21 and current_hand_numeric_user.count (11) >= 1:
            current_hand_numeric_user.remove (11)
            current_hand_numeric_user.append (1)
            user_threshold = sum (current_hand_numeric_user)
        
        if user_threshold < 22:
            computer_card_generated = random.choice (card)
            if computer_card_generated == "J" or computer_card_generated == "Q" or computer_card_generated == "K":
                computer_card_generated_value =  (10)
            elif computer_card_generated == "A":
                computer_card_generated_value =  (11)
            else:
                computer_card_generated_value = (computer_card_generated)

            print (f"The computer has drawn a {computer_card_generated}!")
            print (cards [card.index (computer_card_generated)])
        
            computer_cards.append(computer_card_generated)

            computer_cards_value.append (computer_card_generated_value)

            for index in range (i, len (computer_cards)):
                computer_cards_string += ", " + str (computer_cards [index])

            print (f"The computer\'s hand is: {computer_cards_string}\n")


    computer_threshold = sum(computer_cards_value)
    if computer_threshold > 21 and computer_cards_value.count (11) >= 1:
        computer_cards_value.remove (11)
        computer_cards_value.append (1)
        computer_threshold = sum (computer_cards_value)

    if user_threshold > 21 or computer_threshold > 21 or user_threshold == 21 or computer_threshold == 21:
        continue_game = False

    i += 1

win = False

if user_threshold <= 21:
    if computer_threshold > 21:
        win = True
    elif user_threshold > computer_threshold:
        win = True

equal = False

if user_threshold == computer_threshold:
    equal = True

if win == True and equal == False:
    print ("\nCongratulations! You have won the game!")
    print (victory)
    print (f"Your final hand was {current_hand_user}")

elif win == False and equal == False:
    print ("\nUnfortunately you have lost the game! That's what you get for being too greedy I guess!")
    print (defeat)
    print (f"Your final hand was {current_hand_user}")

else:
    print ("\nIt is a draw.")
    print (draw)
    print (f"Your final hand was {current_hand_user}")




    


