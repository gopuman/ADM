import json
import os
from base64 import b64decode
from pathlib import Path

DATA_DIR = os.getcwd() + "/responses/"
folder_path = DATA_DIR
print(folder_path)
# exit()

# Get a list of all the files in the main folder
files = os.listdir(folder_path)
# Filter the list to only include JSON files
json_files = [folder_path + f for f in files if f.endswith(".json")]
print(json_files)
# Process each JSON file as it is created
for JSON_FILE in json_files:
    # Open the JSON file and load the data
    with open(JSON_FILE, mode="r", encoding="utf-8") as file:
        response = json.load(file)
        print(response)
# JSON_FILE = DATA_DIR / "the h-1679043229.json"
IMAGE_DIR = os.getcwd() +"/images/" #+ JSON_FILE.stem
CHECK_FOLDER = os.path.isdir(IMAGE_DIR)

# If folder doesn't exist, then create it.
if not CHECK_FOLDER:
    os.mkdir(IMAGE_DIR)
    print("created folder : ", IMAGE_DIR)

else:
    print(IMAGE_DIR, "folder already exists.")

# IMAGE_DIR.mkdir(parents=True, exist_ok=True)
print(IMAGE_DIR)
# exit()'
for IDX,JSON_FILE in enumerate(json_files):

    with open(JSON_FILE, mode="r", encoding="utf-8") as file:
        response = json.load(file)
        # print(file.name)

        for index, image_dict in enumerate(response["data"]):
            image_data = b64decode(image_dict["b64_json"])
            image_file = IMAGE_DIR +"/"+ "{}.png".format(IDX)
            with open(image_file, mode="wb") as png:
                png.write(image_data)
