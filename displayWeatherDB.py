import MySQLdb

try:
    connection = MySQLdb.connect(user='weatherfrog', passwd='sunnyDay%%99', db='climate')
    c = connection.cursor()

    c.execute("""
                SELECT *
                FROM BMP280
                GROUP BY timestamp asc;
                """)

    data = c.fetchall()
    for date in data:
        print(date)

    connection.close()
except Exception as ex:
    print(ex)

