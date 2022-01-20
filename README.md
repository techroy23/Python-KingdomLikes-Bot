# Python-KingdomLikes-Bot
Bot for https://kingdomlikes.com that logins into an account and then goes to the youtube views section where it opens and watch by itself all the available videos and then switch to web traffic if there is no more available video

# Prerequisite

 1. Clone this repo
 2. Download python at https://www.python.org/downloads/
 3. Download chromedriver.exe v96.x.xxxx.xx at https://chromedriver.chromium.org/downloads 
 4. Make sure app.py and chromedriver.exe are both in the same directory.
 5. run `pip install selenium`

# How to use

 1. Open config.py then add your kingdomlikes.com credentials
 2. run `python app.py`

# Headless

 - By default the browser window will be hidden.
 - If you want the browser window to show change `headless = "true"` to `headless = "false"`

