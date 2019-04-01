![RSS Feed Tweet Bot](https://raw.githubusercontent.com/gdsoumya/rss_feed_tweet_bot/master/rss_feed_tweet_bot_logo.png)
<br><br>
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)   <img src="https://img.shields.io/badge/made%20with-python-blue.svg" alt="made with python"> [![Codeship Status for gdsoumya/rss_feed_tweet_bot](https://app.codeship.com/projects/4416eed0-2be3-0137-e261-62fb80733f02/status?branch=master)](https://app.codeship.com/projects/331218) <a href='https://github.com/gdsoumya' target='_blank'><img src='https://img.shields.io/github/followers/gdsoumya.svg?label=Folow&style=social'></a><a href="https://twitter.com/intent/tweet?text=Check+out+this+awesome+Github+Repo+for+a+Twitter+Bot%2C+it+can+auto+tweet+posts+using+RSS+Feed+links.&url=https%3A%2F%2Fgithub.com%2Fgdsoumya%2Frss_feed_tweet_bot&hashtags=twitter%2Ctwitter_bot%2Cgithub&original_referer=http%3A%2F%2Fgithub.com%2F&tw_p=tweetbutton" target="_blank">
  <img src="http://jpillora.com/github-twitter-button/img/tweet.png"
       alt="tweet button" title="Check out this awesome Github Repo for a Twitter Bot, it can auto tweet posts using RSS Feed links."></img>
</a>

The 'RSS Feed Tweet Bot' is a single user bot for twitter that automatically posts tweets about new posts/updates using multiple RSS feed links. It has a web interface that streamlines the whole experience.

For a simpler and modular implementation of **RSS Feed Tweet Bot** check out **"[RSS Feed Tweet Bot Lite](https://github.com/gdsoumya/rss_feed_tweet_bot_lite)"**

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

**RSS Feed Tweet Bot** requires [ **Python (> Python 3.6)**](https://www.python.org/) .

### Getting the project.

```sh
$ git clone https://github.com/gdsoumya/rss_feed_tweet_bot.git
or 
Download and extract the Zip-File
```
### Setting up Virtual Environemt
Setting up a virtual environment would be better for both development and normal execution purposes.
```sh
$ cd rss_feed_tweet_bot
$ python -m virtualenv env
$ source env/bin/activate
 or (Windows machine)
$ .\env\Scripts\activate
```
### Installing Dependencies
The Project has a few dependencies which can be installed by running.
```sh
$ pip install -r dependencies.txt 
```
## Starting the Bot
To start the Flask server run
```sh
$ python server.py
```
A Flask development server will be initialized at http://127.0.0.1:5000/

### Warnings 
A possible warning that one might get is :

**WARNING: Do not use the development server in a production environment.**

This warning is displayed because currently a Flask Development Server is running but the default environment of Flask is set to Production, to remove this warning change the FLASK_ENV environment variable.
<br>***Setting environment to development automatically sets the debugger on.**
```sh
$ export FLASK_ENV=development
or (Windows machine)
$ set FLASK_ENV=development
```
## Setting up the Bot
After starting the server for the first time a few things are needed to be setup for it to run properly.
- **Setting up the API Keys** : Visit the settings tab and provide the api keys and tokens. For help regarding setting up a twitter app and getting the API keys check **[this](https://developer.twitter.com/en/docs/basics/developer-portal/overview)**

- **Add RSS Links** : Visit the Feed List tab and add ur RSS Feed links.

After completing the setup just start the bot from the homepage and let it work in the background.

## Errors and Debugging options
The server by default does not start in debugger mode but to initialize debugger mode change the last line of the '[server.py](https://github.com/gdsoumya/rss_feed_tweet_bot/blob/master/server.py)' file to :
```python
app.run() -> app.run(debug=True)
```
Most errors will be logged to the console and can be referenced later for debugging.
## Packages Used
- **[Tweepy](http://www.tweepy.org/)** : For accessing the twitter api.
- **[Flask](http://flask.pocoo.org/)** : For hosting the web interface.
- **[Feedparser](https://pypi.org/project/feedparser/)** : For parsing feeds from RSS links.

## Author
-   **Soumya Ghosh Dastidar**

## Contributting
Any contribution/suggestions are welcomed.
