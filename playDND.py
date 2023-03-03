from chatgpt_wrapper import ChatGPT
from animate import load_animation, stream_text_horizontal
import sys

bot = ChatGPT()

class Story:
    def __init__(self, content, players) -> None:
        self.campaign = content
        self.players = players

    def __str__(self) -> str:
        

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
        pName = input(">> ")
        stream_text_horizontal("Enter Character Class for "+curr_player)
        pCClass = input(">> ")
        stream_text_horizontal("Enter Character Name for "+curr_player)
        pCName = input(">> ")
        Player.players.append(Player(pName, pCClass, pCName))
        print("\n")

    # print(Player.players)

def playDND():
    filename = "identity.txt"
    with open(filename, 'r') as f:
        content = f.read()
    premise_prompt = content.format([i for i in Player.players])

    for chunk in bot.ask_stream(premise_prompt):
        sys.stdout.write(chunk)
        sys.stdout.flush()
    print("\n")

    while(True):
        query = input(">> ")
        for chunk in bot.ask_stream(query):
            sys.stdout.write(chunk)
            sys.stdout.flush()
        print("\n")

if __name__ == '__main__':
    #Play initial animation 
    load_animation()
    #Gather data about players
    get_info()
    #Start the game
    playDND()