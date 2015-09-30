# DataDotPy
A repository dedicated to the development of python programs dealing with data, both big and small.
This is also where different databases will be tested to see which is more effective/efficient.

## TweetMiner
A python program, ran at the command line, built to analyze data mined from Twitter.

You will need to install [tweepy](https://github.com/tweepy/tweepy) to be able to run both versions.

If you wish to use the RethinkDB version, you must install [RethinkDB](http://rethinkdb.com/).
  * Follow all of the instructions!
  * That includes setting up your RethinkDB server.

**How to use:**
_Applies to both versions_
* Configure `TweetCollector.py` to gather the data you want.
  * Type in the name of your database, and table.
  * Type in the hashtags you wish to track(SQLite version only.).
  * If using the CSV method, insert the name of your .csv doc(In the RethinkDB version the csv reader is located in `TweetSifter.py`).
* Run `TweetMiner.py`, but be sure to only run the methods you need.
  * Unless you run the RethinkDB version, then `TweetMiner.py` is set up to allow you to choose what you want.
  * Also, if using the RethinkDB version, you will be prompted to type in the keywords you wish to track and the max number of tweets you would like to collect.
* Import `TweetWrite.py` into a new script and set an instance of `DataFilter()` to analyze and save the data gathered. (Never run `TweetWrite.py` and `TweetMiner.py` at the same time)
  * After an instance of `DataFilter()` is set you can call upon the methods needed to analyze your data as well as store the results.

If you would like to know more about the TweetMiner project, please refer to the [wiki pages](https://github.com/jcode89/DataDotPy/wiki). If you wish to contribute, please, feel free to contact [me](https://github.com/jcode89/DataDotPy/blob/master/CONTACT.md).
