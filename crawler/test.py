import psycopg2

from crawler import settings

def main():
    conn = psycopg2.connect(**settings.DATABASE)
    cur = conn.cursor()
    print('PostgreSQL database version:')
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    print(db_version)
    cur.execute(
        """ CREATE TABLE flat (
            flat_name VARCHAR(50),
            flat_image VARCHAR(250)
        )
        """
    )
    tmp = '''INSERT INTO flat(flat_name, flat_image) VALUES(%s, %s)'''
    data = 'hello', 'image'
    cur.execute(tmp, data)
    cur.close()
    conn.commit()

if __name__ == '__main__':
    main()