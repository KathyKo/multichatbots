<p align="center">
  <img src="https://github.com/KathyKo/multichatbots/blob/main/side%20project%20-%20web/chatbots_banner.png?raw=1" alt="Multichatbots Banner" width="900">
</p>

**Multichatbots**:  
This project is a minimal Flask web application that hosts multiple lightweight AI chatbots behind a single, clean interface. It uses the OpenAI API to power its specialized assistants.

**Key Features**:  
The app provides four different bots, each with a specific purpose:

**🤖 Translator**: Translates text between English (EN) and Traditional Chinese (ZH-TW).  
**🐞 Debugger**: Helps troubleshoot and debug code snippets.  
**📝 Summarizer**: Distills long pieces of text into concise summaries.  
**🧠 General Assistant**: A general-purpose assistant for all other questions.  

## Project Structure
```text
side project - web/
  app.py
  bot_modules/
    bot1.py (translator)
    bot2.py (debugger)
    bot3.py (summarizer)
    bot4.py (gpt)
  templates/
    index.html
    chat.html
  static/
    css/main.css
    js/main.js
    images/*.png
````

*(Modules are imported via `bot_modules/__init__.py`; the Flask app routes `/`, `/chat`, and `/respond`.)*

## Requirements

* Python 3.10+
* Packages: `flask`, `openai`

Install:

```bash
pip install flask openai
```

## Setup

Set your OpenAI API key:

```bash
import openai
openai.api_key = "YOUR_KEY"
```

## Run

```bash
cd "side project - web"
python app.py
```

Open [http://127.0.0.1:5000/](http://127.0.0.1:5000/) and pick a bot from the UI.


