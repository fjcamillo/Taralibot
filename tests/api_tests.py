import psycopg2
import datetime

today = datetime.datetime.now()

def now():
    return datetime.datetime.now()

conn = psycopg2.connect('dbname=taralibotdb user=fjcamillo')

cur = conn.cursor()

#getID = cur.execute('select facebook_id from chat_chatusers where id=1')

cur.execute('INSERT INTO chat_conversations (facebook_fk_id, converse, timestamp) VALUES (%s, %s, %s)',(1, "Hello World!", now()))

conn.commit()

cur.close()

conn.close()

print('---success---')
