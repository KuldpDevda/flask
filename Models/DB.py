from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor


# class DB(object):
# 	"""Initialize mysql database """
# 	host = "localhost"
# 	user = "root"
# 	password = ""
# 	db = "lms"
# 	table = ""

# 	def __init__(self, app):
# 		app.config["MYSQL_DATABASE_HOST"] = self.host;
# 		app.config["MYSQL_DATABASE_USER"] = self.user;
# 		app.config["MYSQL_DATABASE_PASSWORD"] = self.password;
# 		app.config["MYSQL_DATABASE_DB"] = self.db;

# 		self.mysql = MySQL(app, cursorclass=DictCursor)

# 	def cur(self):
# 		return self.mysql.get_db().cursor()

# 	def query(self, q):
# 		h = self.cur()
	
# 		if (len(self.table)>0):
# 			q = q.replace("@table", self.table)

# 		h.execute(q)

# 		return h

# 	def commit(self):
# 		self.query("COMMIT;")


import psycopg2

class DB(object):
    """Initialize PostgreSQL database """
    host = "localhost"
    user = "postgres"
    password = "postgres"
    db = "lms"
    table = ""

    def __init__(self, app):
        app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{self.user}:{self.password}@{self.host}/{self.db}"
        self.conn = psycopg2.connect(
            dbname=self.db,
            user=self.user,
            password=self.password,
            host=self.host
        )

    def cur(self):
        return self.conn.cursor()

    def query(self, q):
        h = self.cur()

        if len(self.table) > 0:
            q = q.replace("@table", self.table)

        h.execute(q)
        return h

    def commit(self):
        self.conn.commit()
