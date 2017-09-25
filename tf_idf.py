import pymysql
import math
from nltk import WhitespaceTokenizer

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="march1009",
    charset='utf8',
    db='tf-idf',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()
tokenizer = WhitespaceTokenizer()

sql_tf = 'SELECT * FROM wiki WHERE id=%s'
sql_idf = 'SELECT COUNT(*) count FROM inverted_index WHERE term=%s'

def tf_idf(id, term):
    cursor.execute(sql_tf, id)
    text = cursor.fetchone()['text']
    words = tokenizer.tokenize(text)
    words = list(map(lambda x: x.lower(), words))
    tf = math.log(1 + words.count(term) / len(words))
    cursor.execute(sql_idf, term)
    idf = 1 / cursor.fetchone()['count']
    print('TF-IDF of the term ' + term + ' in ID=' + str(id) + ': ' + str(tf*idf))

terms = [(41631770, 'also'), (6688599, 'debut'), (13794826, 'language')]
for term in terms:
    tf_idf(*term)

