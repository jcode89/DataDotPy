'''Run this script to gather the data already collected and prep for analysis.
save the user: tweet information to a text file, and finally,
analyze the data gathered and save it to the database.'''

import sqlite3
import datetime

# Open the database connection and gather the data needed for later
conn = sqlite3.connect('TweetData.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS data(Total Tweets,
                                            Actual User,
                                            Tweet User Ratio,
                                            Date Time)''')
fetch = c.execute("select user, text from codenewbie")
total = 0
chat_list = []
actual_user = []
for user, text in fetch:# unpack the tuple
    chat_list.append((user, text.encode('ascii', 'xmlcharrefreplace')))# encode the text properly
    if user not in actual_user:
        actual_user.append(user)
    print(user, text)
    total += 1



# Write the user and the tweet to a txt file.
open_file = open("ChatArchive.txt", 'w')
for text in chat_list:
    # write each line in the list to the file using a double space for each.
    open_file.write((str(text)+ "\n"+"\n"))



# analyze the information gathered from above and save it to the database.
user_num = len(actual_user)
user_ratio = float(total/len(actual_user))
time_now = datetime.datetime.now().strftime("%B, %d, %Y, %X")
print("Number of Tweets: %d" % total)
# Number of users that sent out tweets.
# Multiple tweets per user still count as one user.
print("Number of actual users: %d" % user_num)
# Tweets per user, or Tweets:user
print("Tweets per user: %.2f" % user_ratio)
# Prints exact time programs was run, including the date.
print(time_now)
c.execute("INSERT INTO data VALUES(?,?,?,?)", (total, user_num, user_ratio, time_now))
conn.commit()

# close the file and database connection
open_file.close()
conn.close()
