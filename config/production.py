DEBUG = False
TESTING = False
HOST = 'mydb.c2d6yuy7egrg.us-west-2.rds.amazonaws.com'
PORT = '3306'
USER = 'test_user'
PASSWORD = 'test_user'
DATABASE = 'sample_db'
SQLALCHEMY_DATABASE_URI = 'mysql://' + USER + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE