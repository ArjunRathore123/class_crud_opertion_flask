import psycopg2


def connect_db():
    conn = psycopg2.connect(database="student_db", user="postgres", 
                        password="root", host="localhost", port="5432") 
    return conn

def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL
    );
    '''

    cursor.execute(create_table_query)
    connection.commit()

    cursor.close()
    connection.close()

