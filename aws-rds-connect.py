import psycopg2 as ps
# define credentials 
credentials = {'POSTGRES_ADDRESS' : 'test-db.cup5cgjgpmnt.ap-south-1.rds.amazonaws.com', # change to your endpoint
               'POSTGRES_PORT' : '5432', # change to your port
               'POSTGRES_USERNAME' : 'postgres', # change to your username
               'POSTGRES_PASSWORD' : 'abcdde', # change to your password
               'POSTGRES_DBNAME' : 'test-db'} # change to your db name
# create connection and cursor    
conn = ps.connect(host=credentials['POSTGRES_ADDRESS'],
                  database=credentials['POSTGRES_DBNAME'],
                  user=credentials['POSTGRES_USERNAME'],
                  password=credentials['POSTGRES_PASSWORD'],
                  port=credentials['POSTGRES_PORT'])
cur = conn.cursor()

query = """SELECT * FROM pg_catalog.pg_tables
            WHERE schemaname != 'pg_catalog'
            AND schemaname != 'information_schema';"""
cur.execute(query)
cur.fetchall()