import pymysql
from nltk.tokenize import WhitespaceTokenizer

connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="march1009",
    charset='utf8',
    db='tf-idf',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = connection.cursor()

terms = ['debut', 'two', 'language', 'also']
tokenizer = WhitespaceTokenizer()


sql = 'SELECT * FROM wiki'
cursor.execute(sql)
for record in cursor.fetchall():
    doc_id = record['id']
    text = record['text']
    for term in terms:
        for start, end in tokenizer.span_tokenize(text):
            if text[start:end].lower() == term:
                insert_sql = 'INSERT INTO inverted_index VALUES (%s, %s)'
                cursor.execute(insert_sql, (term, doc_id))
                break


connection.commit()
connection.close()
