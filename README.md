# DataDotPy
A repository dedicated to the development of python programs dealing with data, both big and small.
This is also where different databases will be tested to see which is more effective/efficient.

## TweetMiner
A python program, ran at the command line, built to analyze data mined from Twitter.

You will need to install [tweepy](https://github.com/tweepy/tweepy) to be able to run `TweetMiner.py`

**How to use:**
* Configure `TweetCollector.py` to gather the data you want.
* Run `TweetMiner.py`, but be sure to only run the methods you need.
* Import `TweetWrite.py` into a new script and set an instance of `DataFilter()` to analyze and save the data gathered. (Never run `TweetWrite.py` and `TweetMiner.py` at the same time)
  * After an instance of `DataFilter()` is set you can call upon the methods needed to analyze your data as well as store the results.
