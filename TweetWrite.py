import sqlite3

conn = sqlite3.connect('TweetData.db')
c = conn.cursor()
fetch = c.execute("select user, text from codenewbie")
total = 0
open_file = open("ChatArchive.txt", 'w')
chat_list = []
actual_user = []
for user, text in fetch:# unpack the tuple
    chat_list.append((user, text.encode('ascii', 'xmlcharrefreplace')))# encode the text properly
    if user not in actual_user:
        actual_user.append(user)
    print(user, text)
    total+=1
for text in chat_list:
    open_file.write((str(text)+ "\n"+"\n"))# write each line in the list to the file using a double space for each.
print("Number of Tweets: %d" % total)
# Number of users that sent out tweets.
# Multiple tweets per user still count as one user.
print("Number of actual users: %d" % len(actual_user))
# Tweets per user, or Tweets:user
print("Tweets per user: %.2f:1" % (total/len(actual_user)))
open_file.close()
conn.close()
