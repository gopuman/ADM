import json
import os
import shutil
from base64 import b64decode
from pathlib import Path

import openai
openai.api_key = "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"


def prepare_prompts(fileName):

    file1 = open(fileName, 'r')
    Lines = file1.readlines()

    sentences = Lines[0].strip().split(". ")

    DATA_DIR = Path.cwd() / "responses"
    EXISTS_FOLDER = os.path.exists(DATA_DIR)
    if EXISTS_FOLDER:
        shutil.rmtree(DATA_DIR)

    DATA_DIR.mkdir(exist_ok=True)

    for idx, sentence in enumerate(sentences):

        PROMPT = sentence
        response = openai.Image.create(
            prompt=PROMPT,
            n=1,
            size="256x256",
            response_format="b64_json",
        )
        file_name = DATA_DIR / f"{PROMPT[:5]}-{response['created']}.json"
        with open(file_name, mode="w", encoding="utf-8") as file:
            json.dump(response, file)


def convertJson():

    DATA_DIR = os.getcwd() + "/responses/"
    folder_path = DATA_DIR

    files = os.listdir(folder_path)
    json_files = [folder_path + f for f in files if f.endswith(".json")]

    for JSON_FILE in json_files:
        with open(JSON_FILE, mode="r", encoding="utf-8") as file:
            response = json.load(file)

    IMAGE_DIR = Path.cwd() / "viz/static/images/"
    EXISTS_FOLDER = os.path.exists(IMAGE_DIR)
    if EXISTS_FOLDER:
        shutil.rmtree(IMAGE_DIR)

    IMAGE_DIR.mkdir(exist_ok=True)

    for IDX, JSON_FILE in enumerate(json_files):

        with open(JSON_FILE, mode="r", encoding="utf-8") as file:
            response = json.load(file)
            # print(file.name)

            for index, image_dict in enumerate(response["data"]):
                image_data = b64decode(image_dict["b64_json"])
                image_file = str(IMAGE_DIR) + "/" + "{}.png".format(IDX)
                with open(image_file, mode="wb") as png:
                    png.write(image_data)
