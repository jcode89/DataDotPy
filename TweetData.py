import sqlite3

try:
    conn = sqlite3.connect('TweetData.db')
    c = conn.cursor()
finally:
    conn.close()