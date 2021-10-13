import psycopg2

# Connecting to PostgreSQL database adapter for the Python programming language.

def getConnection():
    conn = psycopg2.connect(
        host="localhost",
        port='5432',
        database="temp",
        user="postgres",
        password="root"
    )
    return conn

def insertdata(finalScrapedData, tablename):
    conn = getConnection()
    cur = conn.cursor()
    for d in finalScrapedData:
        cur.execute("INSERT into webpage(title,subtitle,abstract,download) VALUES (%s, %s, %s,%s)", d)

    conn.commit()
    cur.close()
    conn.close()
