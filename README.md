<h1><p align="center">:robot: ADM - Automated Dungeon Master :joystick:</p></h1>

Welcome to the ADM - Automated Dungeon Master repository! This software allows users to play a game of DND campaign with a fully automated dungeon master powered by AI.

## Installation
```bash
pip install -r requirements.txt
```
- ### [ChatGPT Wrapper](https://github.com/mmabrouk/chatgpt-wrapper)

1. Install the latest version of this software directly from github with pip:

```bash
pip install git+https://github.com/mmabrouk/chatgpt-wrapper
```

2. Install a browser in playwright (if you haven't already). The program will use firefox by default.

```bash
playwright install firefox
```

3. Start up the program in `install` mode. This opens up a browser window. Log in to ChatGPT in the browser window, then stop the program.

```bash
chatgpt install
```

4. Restart the program without the `install` parameter to begin using it.

- ### [DALL-E 2](https://platform.openai.com/docs/introduction)

1. Install the latest OpenAI python bindings.
```bash
pip install openai
```
2. The OpenAI API uses API keys for authentication. Visit your [API Keys](https://platform.openai.com/account/api-keys) page to retrieve the API key you'll use in your requests.


3. Add your API key to the .env file in the root directory of the repository
```bash
OPENAI_API_KEY=<YOUR-API-KEY>
```

## Usage
1. Run the `playDND.py` file to begin the game

```bash
python3 playDND.py
```
## Contributors

<a href="https://github.com/gopuman">
<img src="https://github.com/gopuman.png" width="48">
</a>

<a href="https://github.com/Mahek-jain">
<img src="https://github.com/Mahek-jain.png" width="48">
</a>

<a href="https://github.com/Ruthuvikas">
<img src="https://github.com/Ruthuvikas.png" width="48">
</a>


## License
This project is licensed under the Apache License 2.0. See the LICENSE file for more information.
