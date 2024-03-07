import psycopg2


def connect_db():
    conn = psycopg2.connect(database="student_db", user="postgres", 
                        password="root", host="localhost", port="5432") 
    return conn

def create_table():
    connection = connect_db()
    cursor = connection.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS student (
        id SERIAL PRIMARY KEY,
        student_name VARCHAR(100), contact varchar(10),address varchar(100) ,
        college_name VARCHAR(100)
    );
    '''

    cursor.execute(create_table_query)
    connection.commit()

    cursor.close()
    connection.close()

