<h1><p align="center">:robot: ADM - Automated Dungeon Master :joystick:</p></h1>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10-blue.svg" alt="Python version">
  <img src="https://img.shields.io/github/repo-size/gopuman/ADM" alt="Repo size">
</p>

Welcome to ADM - Automated Dungeon Master repository! ADM allows users to play a game of DND campaign with a fully automated dungeon master powered by GPT-3.

## Installation
To install the required packages, run the following command:
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

<table>
  <tr>
    <td align="center"><a href="https://github.com/gopuman"><img src="https://github.com/gopuman.png" width="100px;" alt=""/><br /><sub><b>Gopal</b></sub></a></td>
    <td align="center"><a href="https://github.com/Mahek-jain"><img src="https://github.com/Mahek-jain.png" width="100px;" alt=""/><br /><sub><b>Mahek</b></sub></a></td>
    <td align="center"><a href="https://github.com/Ruthuvikas"><img src="https://github.com/Ruthuvikas.png" width="100px;" alt=""/><br /><sub><b>Ruthuvikas</b></sub></a></td>
  </tr>
</table>

## Future Work (To do)
- [ ] In-game Text-to-speech voiceover
- [ ] Speech-to-text input
- [ ] Input as character sheet
- [ ] Dynamic music generation
- [ ] Stable Diffusion over DALL-E

## License
This project is licensed under the Apache License 2.0. See the LICENSE file for more information.
