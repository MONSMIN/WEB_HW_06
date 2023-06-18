import glob
import sqlite3
from prettytable import PrettyTable


def read_sql_script(filename):
    conn = sqlite3.connect('hw_06.sqlite')
    cursor = conn.cursor()

    with open(filename, 'r') as file:
        sql = file.read()
    cursor.execute(sql)

    results = cursor.fetchall()
    if len(results) == 0:
        print("Результати: Запит не повернув жодного запису.")
    else:
        columns = [description[0] for description in cursor.description]
        table = PrettyTable(columns)
        for row in results:
            table.add_row(row)
        print("Результати:")
        print(table)

    conn.close()


if __name__ == '__main__':
    file_list = glob.glob('query_*.sql')

    if len(file_list) == 0:
        print("Немає доступних SQL-скриптів.")
    else:
        print(f"Знайдено {len(file_list)} SQL-скриптів.")

        query_descriptions = {
            'query_1.sql': 'Знайти 5 студентів із найбільшим середнім балом з усіх предметів.',
            'query_2.sql': 'Знайти студента із найвищим середнім балом з певного предмета.',
            'query_3.sql': 'Знайти середній бал у групах з певного предмета.',
            'query_4.sql': 'Знайти середній бал на потоці (по всій таблиці оцінок).',
            'query_5.sql': 'Знайти, які курси читає певний викладач.',
            'query_6.sql': 'Знайти список студентів у певній групі.',
            'query_7.sql': 'Знайти оцінки студентів в окремій групі з певного предмета.',
            'query_8.sql': 'Знайти середній бал, який ставить певний викладач зі своїх предметів.',
            'query_9.sql': 'Знайти список курсів, які відвідує студент.',
            'query_10.sql': 'Список курсів, які певному студенту читає певний викладач.',
            'query_11.sql': 'Середній бал, який певний викладач ставить певному студентові.',
            'query_12.sql': 'Оцінки студентів у певній групі з певного предмета на останньому занятті.',
        }

        print("Доступні SQL-скрипти:")
        for i, filename in enumerate(file_list):
            print(f"  {i + 1}. {filename}")

        files = {
            1: 'query_1.sql',
            2: 'query_2.sql',
            3: 'query_3.sql',
            4: 'query_4.sql',
            5: 'query_5.sql',
            6: 'query_6.sql',
            7: 'query_7.sql',
            8: 'query_8.sql',
            9: 'query_9.sql',
            10: 'query_10.sql',
            11: 'query_11.sql',
            12: 'query_12.sql'
        }

        while True:
            user_input = input("Введіть номер запиту для виконання (1-12) або 'exit' для виходу: ")

            if user_input == "exit":
                print("Бувай")
                break

            if user_input.isdigit() and int(user_input) in files:
                selected_file = files[int(user_input)]
                print("Обраний SQL-скрипт:", selected_file)
                print("Опис запиту:", query_descriptions[selected_file])

                with open(selected_file, 'r') as file:
                    sql_script = file.read()
                    print("Вміст SQL-скрипту:")
                    print(sql_script)
                    read_sql_script(selected_file)
            else:
                print("Некоректний ввід. Будь ласка, введіть число від 1 до 12.")
