import psycopg2
import datetime

def now():
    return datetime.datetime.now()

class postgrecommands:

    def __init__(self, fbid, message):
        self.conn = psycopg2.connect('dbname=taralibotdb user=fjcamillo')
        self.cur = self.conn.cursor()


    def insert_conversation(self, fbid, message):

        self.cur.execute('INSERT INTO chat_conversations (facebook_fk_id, converse, timestamp) VALUES (%s, %s, %s)',)