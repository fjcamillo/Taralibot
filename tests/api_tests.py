import psycopg2
import datetime

today = datetime.datetime.now()

conn = psycopg2.connect('dbname=taralibotdb user=fjcamillo')

cur = conn.cursor()

cur.execute('INSERT INTO chat_conversations (, converse) VALUES (%s, %s)',('firstuser', 'Hello World!'))

conn.commit()

cur.close()

conn.close()

print('---success---')
