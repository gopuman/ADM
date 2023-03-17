from chatgpt_wrapper import ChatGPT
from animate import load_animation, stream_text_horizontal
from campaign import cleanup, save
from runflask import runFlask
import sys
import importlib

bot = ChatGPT()

class Story:
    # Return the story to the summarizer.
    def __init__(self, content) -> None:
        self.campaign = content

    def __str__(self):
        return ' '.join(self.campaign)

    def saveGame(self):
        formatted_campaign = cleanup(self.__str__())
        filename = save(formatted_campaign)
        self.summarizeCampaign(filename)

    def summarizeCampaign(self, storyFile):
        summarizer = importlib.import_module("bert-cnn")
        summarizer.bert_model(storyFile)

class Player:
    _idx = 0
    players = []

    def __init__(self, playerName, charClass, charName, charRace) -> None:
        Player._idx += 1
        self.idx = self._idx
        self.playerName = playerName
        self.charClass = charClass
        self.charName = charName
        self.charRace = charRace

    def __str__(self) -> str:
        return "Player {} -> Name:{}, Character Class:{}, Character Name:{}, Character Race:{}".format(self.idx, self.playerName, self.charClass, self.charName, self.charRace)

    def __repr__(self) -> str:
        return self.charName + " the " + self.charClass + " of " + self.charRace + " race"


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
        stream_text_horizontal("Enter Character Race for "+curr_player)
        pCRace = input(">> ")
        Player.players.append(Player(pName, pCClass, pCName, pCRace))
        print("\n")


def playDND():
    campaign = []
    prem = []

    filename = "identity2.txt"
    with open(filename, 'r') as f:
        content = f.read()
    premise_prompt = content.format([i for i in Player.players])

    for chunk in bot.ask_stream(premise_prompt):
        prem.append(chunk)
        sys.stdout.write(chunk)
        sys.stdout.flush()
    campaign.append("".join(prem))
    print("\n")

    while (True):
        chunks = []
        query = input(">> ")
        if (query == "quit"):
            story = Story(campaign)
            # print(story)
            story.saveGame()
            runFlask()
            break
        for chunk in bot.ask_stream(query):
            chunks.append(chunk)
            sys.stdout.write(chunk)
            sys.stdout.flush()
        campaign.append("".join(chunks))
        print("\n")


if __name__ == '__main__':
    # Play initial animation
    load_animation()
    # Gather data about players
    get_info()
    # Start the game
    playDND()
