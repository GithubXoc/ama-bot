import psycopg


class Database:
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.port = port

    def connect(self):
        return psycopg.connect(
            host=self.host,
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            port=self.port
        )
    
    def execute_query(self, query):
        with self.connect() as conn:
            with conn.cursor() as cur:
                cur.execute(query)
                return cur.fetchall()