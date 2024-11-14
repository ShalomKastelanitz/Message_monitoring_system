import psycopg2




pg_conn = psycopg2.connect("dbname='email_db' user='user' password='password'")
pg_cursor = pg_conn.cursor()