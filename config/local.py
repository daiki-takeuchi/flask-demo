DEBUG = True
TESTING = True
HOST = 'localhost'
PORT = '3306'
USER = 'test_user'
PASSWORD = 'test_user'
DATABASE = 'sample_db'
SQLALCHEMY_DATABASE_URI = 'mysql://' + USER + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE
