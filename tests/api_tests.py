import psycopg2
import datetime

today = datetime.datetime.now()

conn = psycopg2.connect('dbname=taralibotdb user=fjcamillo')

cur = conn.cursor()

cur.execute('INSERT INTO chat_chatusers (facebook_id, facebook_image) VALUES (%s, %s)',('firstuser', ' '))

conn.commit()

cur.close()

conn.close()

print('---success---')
