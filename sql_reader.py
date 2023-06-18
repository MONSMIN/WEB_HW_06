import sqlite3
import glob



def read_sql_script():
    conn = sqlite3.connect('hw_06.sqlite')
    cursor = conn.cursor()

    with open('query_2.sql', 'r') as file:
        sql = file.read()
    cursor.execute(sql)

    results = cursor.fetchall()
    for r in results:
        print(r)

    conn.close()

if __name__ == '__main__':
    print("1 Скрипт :")
    read_sql_script()
    print("*" * 50)


