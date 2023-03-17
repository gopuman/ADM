import os


def cleanup(campaign):
    return campaign


def save(formatted_campaign):
    counter = 0
    filename = "stories/story_{}.txt"
    while os.path.isfile(filename.format(counter)):
        counter += 1
    filename = filename.format(counter)

    with open(filename, 'w') as f:
        f.write(formatted_campaign)

    return filename
