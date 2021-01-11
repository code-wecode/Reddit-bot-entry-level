# Overview
A bot that listen for new post on subreddit then scan for keywords from post title. If found match, message the post author

## Requirement
- Python 3+

### Instruction
- Windows
    In the current working directory(where this project is) open your CMD and `cd` to project directory then run `pip3 install -r requirements.txt`
- Linux
    Point your terminal to the projects directory and run `pip install -r requirements.txt`

#### Setup
All the settings needed to run the bot are contained inside **config.json** and **praw.ini**
- config.json 
    In the file are the name-value paired that value need to be added to. Add the values as needed(they're self explanatory) then run the bot
- praw.ini 
    - `praw.ini` is how the bot authenticate with your reddit account. To begin, head to [Here](https://www.reddit.com/prefs/apps) and click the create app button. Give it a name and select **script** from the radio options. add description(if you want) and for the about url field, leave it blank. Finally, write **`http://127.0.0.1/redirect`** into the last field(redirect uri) and click **Create app**
    - Now, open `praw.ini` file and add value to the **[bot1]** section in the file(bottom of the file).
    **client_id** and **client_secret** are in the script you created on your reddit account. Enter your reddit **username** and **password** at the fields in the section and for the rest of the fields, just come up with values for them.


##### Run
To run the bot,
- Windows
    `Python bot.py`
- Linux
    `python3 bot.py`