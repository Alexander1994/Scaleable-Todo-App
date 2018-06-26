
import psycopg2, atexit

dbname = "scaleable_todo_app"
user = "postgres"

try:
    conn = psycopg2.connect("dbname={} user={}".format(dbname, user))
except:
    print("db connection failled")

curr = conn.cursor()

def login(username, password):
    SQL = """SELECT id 
             FROM Users
             WHERE email = %s
             AND password = crypt(%s, password);
          """
    data = (username, password)
    curr.execute(SQL, data)
    return curr.fetchone() != None # true if login success

def shutdown_hook():
    curr.close()
    conn.close()
    print("db connections shutdown")


def test():
    print("hello modeuls top level")

atexit.register(shutdown_hook)