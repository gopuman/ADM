from chatgpt_wrapper import ChatGPT
from animate import load_animation, stream_text_horizontal
import sys

# bot = ChatGPT()

class Player:
    _idx = 0
    players = []

    def __init__(self, playerName, charClass, charName) -> None:
        Player._idx += 1
        self.idx = self._idx
        self.playerName = playerName
        self.charClass = charClass
        self.charName = charName

    def __str__(self) -> str:
        return "Player {} -> Name:{}, Character Class:{}, Character Name:{}".format(self.idx, self.playerName, self.charClass, self.charName)

    def __repr__(self) -> str:
        return self.charName + " the " + self.charClass


def get_info():
    
    welcome_prompt = "Greetings, adventurers! Are you ready to embark on a journey into the realm of DnD?"
    stream_text_horizontal(welcome_prompt)

    etc = "Press Enter to continue..."
    stream_text_horizontal(etc)
    input()

    player_prompt = "How many players are in for today's adventure?"
    stream_text_horizontal(player_prompt)
    n_players = int(input(">> "))
    print("\n")

    for i in range(n_players):
        curr_player = "Player " + str(i+1)
        stream_text_horizontal("Enter Name for "+curr_player)
        pName = input()
        stream_text_horizontal("Enter Character Class for "+curr_player)
        pCClass = input()
        stream_text_horizontal("Enter Character Name for "+curr_player)
        pCName = input()
        Player.players.append(Player(pName, pCClass, pCName))
        print("\n")

    print(Player.players)

def playDND():
    premise_prompt = "You are ADM the dungeon master for a game of dungeons and dragons. You will run the campaign by beginning with a descriptive scenario, and carry on from there. At each point of the story you will ask the players to decide how they would like to proceed and carry the story forward from there. You will also include battle scenes where the players can choose to roll a die in person or generate a random number. Players will have to have handy their character traits and proficiency card for when it is needed. Also include ability checks throughout the campaign. The characters taking part in today's session are:{}. Begin by introducing yourself".format([i for i in Player.players])
    for chunk in bot.ask_stream(premise_prompt):
        sys.stdout.write(chunk)
        sys.stdout.flush()

    while(True):
        query = input(">> ")
        for chunk in bot.ask_stream(query):
            sys.stdout.write(chunk)
            sys.stdout.flush()

if __name__ == '__main__':
    #Play initial animation 
    #load_animation()
    #Gather data about players
    get_info()
    #Start the game
    # playDND()