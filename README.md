# TerminalTwitter (TT)

TerminalTwitter is a very simple command-line Twitter client. It shows latest tweets from timeline in the terminal.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tweepy library. (You may need to use pip3 for Python3)

```bash
pip3 install tweepy
```

## Usage
* Consumer API keys, access token and access token secret must be saved in a JSON file in the same directory with the script.

**Sample JSON file:**
```
# keys.json
{ "consumer_key": "API_KEY",
  "consumer_secret": "API_SECRET_KEY", 
  "access_token": "ACCESS_TOKEN",
  "access_token_secret": "ACCESS_TOKEN_SECRET" }
```

* To change the settings, run it with '--settings' argument:
```
$python3 main.py --settings
```

* Run the script with python3:
```
$python3 main.py
```

## Contributing
This work is still in progress. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
