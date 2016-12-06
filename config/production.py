DEBUG = False
TESTING = False
HOST = '104.198.126.171'
PORT = '3306'
USER = 'test_user'
PASSWORD = 'test_user'
DATABASE = 'sample_db'
SQLALCHEMY_DATABASE_URI = 'mysql://' + USER + ':' + PASSWORD + '@' + HOST + ':' + PORT + '/' + DATABASE
