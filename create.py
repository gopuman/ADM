import json
import os
from pathlib import Path

import openai

fileName = 'summaries/summary_0.txt'
file1 = open(fileName, 'r')
Lines = file1.readlines()
print(Lines,"lines",len(Lines),Lines[0])
print("####################",file1.readline())
print("file readlines",Lines[0].strip().split(". "))
# Read the first paragraph and split by newline character (\n)
#first_paragaph = Lines[0]
sentences = Lines[0].strip().split(". ")#file1.readline().strip().split("\n")
# print("jnfcjfrnjfnfjrnejvidjfv",first_paragraph,first_paragraph[0])
 # Split the first paragraph into sentences using period (.) as a delimiter
# sentences = first_paragraph.split(". ")
print(type(sentences),len(sentences))
for idx,sentence in enumerate(sentences):
    print("sentence no",idx,type(sentence),sentence,"\n############sanity check for sentence and their types individually############")
    # exit()
    PROMPT = sentence
#PROMPT = "the heroes emerged from the cult's lair, exhausted but victorious."
    DATA_DIR = Path.cwd() / "responses"
    DATA_DIR.mkdir(exist_ok=True)
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Image.create(
        prompt=PROMPT,
        n=1,
        size="256x256",
        response_format="b64_json",
    )
    file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"
    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response, file)
