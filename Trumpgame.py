import random

class Card(object):
    def __init__(self, name, sportsmanship, strength, toprating, toughness ):
        self.name          = name
        self.sportsmanship = sportsmanship
        self.strength      = strength
        self.toprating     = toprating
        self.toughness     = toughness

    def show(self):
        print("**** {} ****".format(self.name))
        print("Strenght:         {}".format(self.strength) )
        print("Sportsmanship:    {}".format(self.sportsmanship ))
        print("Toprating:        {}".format(self.toprating))
        print("Toughness:        {}".format(self.toughness))

    def get_characterstic(self, characerstic):
        if  characerstic ==  "sportsmanship":
            return  self.sportsmanship
        elif characerstic == "strength":
            return  self.strength
        elif characerstic == "toprating":
            return self.toprating
        elif characerstic == "toughness":
            return self.toughness


class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.cards = []
        self.dicenumber = 0
        self.selected_charcterstic =  None
        self.has_next_move = False
        self.points = 0
        self.is_god_spell_open = True
        self.is_resurrect_spell_open = True

    def display(self):
        print("Name of the player is {}".format(self.name) )

    def show(self):

        print("<<----------->> {}'s D E C K  <<----------->>".format(self.name))
        for c in self.cards:
            c.show()
        print("<<----------->> E N D of the D E C K  <<----------->>")

    def roll_dice(self):

        print("{}... Do you want roll the Dice? Please enter (Y) to proceed and (N) to exit the game :-)".format( self.name))
        while True:
           action = input()
           if ( action == 'Y'):
                self.dicenumber = random.randint(1, 6)
                print('Your number is {}'.format(self.dicenumber))
                break
           elif ( action == 'N'):
                print("Bye..Bye")
                quit()
           else:
                print("Please enter a valid input. Enter (Y) to proceed and (N) to exit the game ")


    def draw(self):
        return self.cards.pop(1)


    def select_move(self):

        while True:
            if  self.is_god_spell_open == True :
                print("Select 'n' for Normal spell")
                print("Select 'g' for God spell")
                move = input()
            elif self.is_god_spell_open == False :
                move = "n"

            if (move != 'g' and move != 'n' ):
                print("Please enter a valid input")
            else:
                break

        if  move == 'g':
            self.is_god_spell_open = False

        return move

    def challange(self):
        self.has_next_move = False
        print("<---------->Your drawn card is <---------->")
        self.cards[0].show( )
        print("Select the characterstic you want to challenage")
        print("a for Strength")
        print("b for Sportsmanship")
        print("c for Toprating")
        print("d for Toughness")


        while True:
            characterstic = input()
            if ( characterstic == "a" or characterstic == "b" or characterstic == "c" or characterstic == "d" ):
                if characterstic == "a":
                    self.selected_charcterstic = "strength"
                elif characterstic == "b":
                    self.selected_charcterstic = "sportsmanship"
                elif characterstic == "c":
                    self.selected_charcterstic = "toprating"
                elif characterstic == "d":
                    self.selected_charcterstic = "toughness"

                return self.selected_charcterstic
                break
            else:
                print("Please enter a valid input.")
                print("Select the characterstic you want to challenage")
                print("a for Strength")
                print("b for Sportsmanship")
                print("c for Toprating")
                print("d for Toughness")


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
        self.player1 = Player( )
        self.player2 = Player( )


    def build(self):
        for s in ["John Cena", "Seth Rollins","Brock Lensar","Alexa Bliss","Gold Dust","Under Taker","Tyson Kidd","Nikki Bella", "Randy Orton", "The Rock"]:
                if len(self.cards) == 0:
                    self.cards.append(Card(s,  -1, -2, -3, -4))
                elif len(self.cards) % 2 == 0:
                    self.cards.append(Card(s, len(self.cards) ** 1, len(self.cards) ** 2, len(self.cards) ** 3, len(self.cards) ** 4))
                elif len(self.cards) % 2 == 1:
                    self.cards.append(Card(s, len(self.cards) * 1, len(self.cards) * 2, len(self.cards) * 3, len(self.cards) * 4))

    def show(self):

        print("<<----------->> S T A R T of the D E C K  <<----------->>")
        for c in self.cards:
            c.show()
        print("<<----------->> E N D of the D E C K  <<----------->>")


    def shuffle(self):
        for i in range(len(self.cards)-1, 0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def distribute(self, player1, player2):
        self.shuffle()
        print("<<----------->> IN DISTRIBUTION  <<----------->>")
        self.player1 = player1
        self.player2 = player2

        print("Total card {}",format(len(self.cards)))
        lv_count = len(self.cards) / 2
        print("Each player gets {}", format(lv_count))

        for i in range(0,len(self.cards)):
            if  i % 2 == 0:
                self.player1.cards.append(self.cards[i])
            else:
                self.player2.cards.append(self.cards[i])

def draw(self):
        return self.cards.pop()


class Game(object):
    def __init__(self):
        self.player1 = Player( )
        self.player2 = Player( )
        self.deck    = Deck( )
        self.sel_charcterstic = None
        self.outdated_cards = []

    def get_players(self):
        i = 1
        while True:
            print("Please enter name of the player {}". format(i))
            name = input()

            if (i == 1):
                self.player1.name = name
                i = i + 1
            elif (i == 2):
                self.player2.name = name
                i = i + 1

            if (i > 2):
                break

    def play(self):

        self.get_players()
        self.deck.distribute(self.player1, self.player2)

        print("Lets Roll the Dice ... to see who will start the Game :-)")

        while True:
            self.player1.roll_dice()
            self.player2.roll_dice()
            if  ( self.player1.dicenumber == self.player2.dicenumber ):
                print("Sorry Guys... both of drawn same numbers.... Roll the Dice Again")
            elif ( self.player1.dicenumber > self.player2.dicenumber):
                print("{} will start the game".format(self.player1.name))
                self.player1.has_next_move = True
                break
            elif ( self.player1.dicenumber < self.player2.dicenumber ):
                print("{} will start the game".format(self.player2.name))
                self.player2.has_next_move = True
                break

        while len(self.player1.cards) > 0 or len(self.player1.cards) > 0:
            if self.player1.has_next_move:
                if  (self.player1.is_resurrect_spell_open == True and len(self.outdated_cards) > 0 ):
                    resurrect = self.select_resurrect()
                    if  resurrect == 'y':
                        lv_index = random.randint(0, len(self.outdated_cards)-1)
                        self.player1.cards.insert(0,self.outdated_cards[lv_index])
                        self.outdated_cards.pop(lv_index)
                        self.player1.is_resurrect_spell_open == False
                self.sel_charcterstic = self.player1.challange()
                move = self.player1.select_move()
                if  move == 'g':
                    print("Which card you want to choose from {}".format(self.player2.name))
                    while True:
                        print("selct from 1 to {} card".format(len(self.player2.cards)))
                        choosen_card = int( input( ) )
                        if ( choosen_card >= 1 and choosen_card <= len(self.player2.cards)):
                            break
                        else:
                            print("enter a valid input")
                    p1_card = 0
                    p2_card = choosen_card
                else:
                    p1_card = 0
                    p2_card = 0



            elif self.player2.has_next_move:
                if  (self.player2.is_resurrect_spell_open == True and len(self.outdated_cards) > 0 ):
                    resurrect = self.select_resurrect()
                    if  resurrect == 'y':
                        lv_index = random.randint(0, len(self.outdated_cards)-1)
                        self.player2.cards.insert(0,self.outdated_cards[lv_index])
                        self.outdated_cards.pop(lv_index)
                        self.player2.is_resurrect_spell_open == False

                self.sel_charcterstic = self.player2.challange()
                move = self.player2.select_move()
                if move == 'g':
                    print("Which card you want to choose from {}".format(self.player1.name))
                    while True:
                        print("selct from 1 to {} card".format(len(self.player1.cards)))
                        choosen_card = int( input( ) )
                        if (choosen_card >= 1 and choosen_card <= len(self.player1.cards)):
                            break
                        else:
                            print("enter a valid input")
                    p1_card = 0
                    p2_card = choosen_card
                else:
                    p1_card = 0
                    p2_card = 0

            self.compare(p1_card, p2_card)

        self.display_score()



    def compare(self, p1_card:0,p2_card:0):
        if self.player1.cards[p1_card].get_characterstic(self.sel_charcterstic) < self.player2.cards[p2_card].get_characterstic(self.sel_charcterstic):
            print("{} won the challenge".format(self.player2.name))
            self.player2.points =  self.player2.points + 1
            self.player1.has_next_move = False
            self.player2.has_next_move = True
        else:
            print("{} won the challenge".format(self.player1.name))
            self.player1.points = self.player1.points + 1
            self.player1.has_next_move = True
            self.player2.has_next_move = False

        # Add to outdated deck
        self.outdated_cards.append(self.player1.cards[p1_card])
        self.outdated_cards.append(self.player2.cards[p2_card])

        # Remove from player's Deck

        self.player1.cards.pop(p1_card)
        self.player2.cards.pop(p2_card)

    def select_resurrect(self):
        while True:
            print("Enter y to proceed with Resurrcet and n to continue normall")
            move = input()
            if  (move != 'y' and move != 'n' ):
                print("Please enter a valid input")
            else:
                break
        return move

    def display_score(self):
        print("{} score:".format(self.player1.name))
        print("{}".format(self.player1.points))
        print("{} score:".format(self.player2.name))
        print("{}".format(self.player2.points))

        if self.player2.points > self.player1.points:
            print("{} won the game".format(self.player2.name))
        else:
            print("{} won the game".format(self.player1.name))




trumpgame = Game( )
trumpgame.play()

# deck = Deck( )
# deck.show()
#
#
# deck.shuffle()
# deck.show()
#
# deck.distribute("Anil","Sneha")
# # card = deck.draw()
# # card.show()
#
# player1 = Player("Anil")
# player1.roll_dice()



