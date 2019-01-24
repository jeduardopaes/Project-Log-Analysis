import psycopg2

try:
    db = psycopg2.connect("dbname=news")
except psycopg2.Error as e:
    print ("Unable to connect to the database")


def most_accessed_articles():
    # --What are the most popular three articles of all time?
    cursor = db.cursor()

    cursor.execute("Select * from most_accessed_articles")

    results = cursor.fetchall()

    return results


def most_accessed_authors():
    # --Who are the most popular article authors of all time?
    cursor = db.cursor()

    cursor.execute("select * from most_accessed_authors")

    results = cursor.fetchall()

    return results


def percent_erros_per_day():
    # --On which days did more than 1% of requests lead to errors?
    cursor = db.cursor()

    cursor.execute("select * from percent_erros_per_day where percent > 1;")

    results = cursor.fetchall()

    return results


def closeConnection():
    db.close()
