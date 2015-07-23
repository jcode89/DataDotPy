import sqlite3

conn = sqlite3.connect('TweetData.db')
c = conn.cursor()
fetch = c.execute("select user, text from codenewbie")
total = 0
open_file = open("ChatArchive.txt", 'w')
chat_list = []
for date, text in fetch:# unpack the tuple
    chat_list.append((date, text.encode('ascii', 'xmlcharrefreplace')))# encode the text properly
    print(date, text)
    total+=1
for text in chat_list:
    open_file.write((str(text)+ "\n"+"\n"))# write each line in the list to the file using a double space for each.
print(total)
open_file.close()
conn.close()