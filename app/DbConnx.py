

# create a class to encapsulate the database connection
# enhancements include the ability to pass in the connection parameters from the calling program
class DbConnx:
    def __init__(self, db_host="marvelgetwell.cs1gposyeo3a.us-east-1.rds.amazonaws.com", db_name="postgres", db_user="getwell", db_password="Voltron*09", db_port="5432"
                 ):
        self.db_host = db_host
        self.db_name = db_name
        self.db_user = db_user
        self.db_password = db_password
        self.db_port = db_port
        self.conn = None
        self.cur = None

    def connect(self):
        import psycopg2
        self.conn = psycopg2.connect(host=self.db_host, database=self.db_name,
                                     user=self.db_user, password=self.db_password, port=self.db_port)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def execute(self, query, params=None):
        if params:
            self.cur.execute(query, params)
        else:
            self.cur.execute(query)

    def fetchall(self):
        rows = self.cur.fetchall()
        return rows
