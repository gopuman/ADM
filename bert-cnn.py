
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def distilbert_model(storyfile):
    tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
    model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")

    # storyPath = "stories/" + storyfile
    storyPath = storyfile
    f = open(storyPath, "r")
    STORY = f.read()
    # inputs = tokenizer("summarize: " + STORY, return_tensors="pt", max_length=10000, truncation=True)
    inputs = tokenizer(STORY, return_tensors="pt", truncation=True)
    outputs = model.generate(
        inputs["input_ids"], max_length=400, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False
    )

    summary = tokenizer.decode(outputs[0])
    summary = summary.strip('</s>')
    summary = summary.strip('<s>')
    summary += '\n\n\n'

    sf = storyfile.strip(".txt")
    sf = sf.split("_")
    summaryName = 'summary' + '_' + sf[1]

    summaryFilename = 'summaries/' + summaryName + '.txt'
    f = open(summaryFilename, "a")
    f.write(summary)
    f.close()

    return summary

def googleT5_model(storyfile):

    model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")
    tokenizer = AutoTokenizer.from_pretrained("t5-base")

    # storyPath = "stories/" + storyfile
    storyPath = storyfile
    f = open(storyPath, "r")
    STORY = f.read()

    # T5 uses a max_length of 512 so we cut the article to 512 tokens.
    inputs = tokenizer("summarize: " + STORY, return_tensors="pt", max_length=10000, truncation=True)
    outputs = model.generate(
    inputs["input_ids"], max_length=400, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False
    )

    summary = tokenizer.decode(outputs[0])
    summary = summary.strip('<pad>')
    summary = summary.strip('</s>')
    summary += '\n\n\n'
    sf = storyfile.strip(".txt")
    sf = sf.split("_")
    summaryName = 'summary' + '_' + sf[1]

    summaryFilename = 'summaries/' + summaryName + '.txt'
    f = open(summaryFilename, "a")
    f.write(summary)
    f.close()

    return summary

def bert_model(storyfile):

    tokenizer = AutoTokenizer.from_pretrained("philschmid/bart-large-cnn-samsum")
    model = AutoModelForSeq2SeqLM.from_pretrained("philschmid/bart-large-cnn-samsum")

    # storyPath = "stories/" + storyfile
    storyPath = storyfile
    f = open(storyPath, "r")
    STORY = f.read()
    # inputs = tokenizer("summarize: " + STORY, return_tensors="pt", max_length=100000, truncation=True)
    inputs = tokenizer(STORY, return_tensors="pt", truncation=True)
    outputs = model.generate(
        inputs["input_ids"], max_length=400, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=False
    )

    summary = tokenizer.decode(outputs[0])
    summary = summary.strip('</s>')
    summary = summary.strip('<s>')
    summary += '\n\n\n'

    sf = storyfile.strip(".txt")
    sf = sf.split("_")
    summaryName = 'summary' + '_' + sf[1]

    summaryFilename = 'summaries/' + summaryName + '.txt'
    f = open(summaryFilename, "a")
    f.write(summary)
    f.close()

    return summary


# for i in range(0, 10):
#     STORY_NAME = 'story_' + str(i) + '.txt'

#     summary_bert = bert_model(STORY_NAME)

#     print('Bert-cnn generated summary: \n')
#     print(summary_bert)

#     summary_googleT5 = googleT5_model(STORY_NAME)

#     print('google T5 generated summary: \n')
#     print(summary_googleT5)

#     summary_distilbert = distilbert_model(STORY_NAME)

#     print('distilbert generated summary: \n')
#     print(summary_distilbert)
