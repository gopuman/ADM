
from transformers import pipeline

"""# 1. Load Summarization Pipeline"""

summarizer = pipeline("summarization")

"""# 2. Summarize Text"""

ARTICLE = """ 
Our story begins in the outskirts of the kingdom of Arathia, where two adventurers, Mando the Merlin and Mike the Barbarian, meet in a tavern. They strike up a conversation and realize that they have a common goal: to rid the kingdom of an evil sorcerer named Zoltar. They decide to team up and embark on a quest to find and defeat Zoltar.
Their journey takes them through the dense forest of Arathia. As they walk, they hear the sound of battle in the distance. They approach the sound and see a group of armed men attacking a lone guard.
Mando and Mike decide to intervene and attack the armed men. They manage to defeat all but one of the attackers, who is wounded but still standing. Mike moves in to attack the wounded guard with his greatsword, but misses. The guard retaliates, but his attack misses as well.
Mando attempts to disarm the guard with a spell, but instead decides to use the Forbidden Death Curse spell. He chooses to sacrifice his comrade, Mike, in order to cast the spell. However, the spell backfires and hits Mando, killing him.
Mike, horrified by what has just happened, kills Mando in self-defense. The campaign ends abruptly, with Mike standing alone in the forest, haunted by the events of that day.
"""

summarizer(ARTICLE, max_length=250, min_length=30, do_sample=False)

summarizer(ARTICLE, max_length=279, min_length=30, do_sample=True)

"""#Google T5"""

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
tokenizer = AutoTokenizer.from_pretrained("t5-base")

# T5 uses a max_length of 512 so we cut the article to 512 tokens.
inputs = tokenizer("summarize: " + ARTICLE, return_tensors="pt", max_length=10000, truncation=True)
outputs = model.generate(
    inputs["input_ids"], max_length=400, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False
)

print(tokenizer.decode(outputs[0]))

"""#google/pegasus-xsum"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("google/pegasus-xsum")
model = AutoModelForSeq2SeqLM.from_pretrained("google/pegasus-xsum")

inputs = tokenizer("summarize: " + ARTICLE, return_tensors="pt", max_length=10000, truncation=True)
outputs = model.generate(
    inputs["input_ids"], max_length=400, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False
)

print(tokenizer.decode(outputs[0]))

"""#philschmid/bart-large-cnn-samsum"""

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")
model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum")

inputs = tokenizer("summarize: " + ARTICLE, return_tensors="pt", max_length=10000, truncation=True)
outputs = model.generate(
    inputs["input_ids"], max_length=400, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False
)

print(tokenizer.decode(outputs[0]))