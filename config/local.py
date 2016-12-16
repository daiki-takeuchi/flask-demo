DEBUG = True
TESTING = True

# Google Cloud Project ID
PROJECT_ID = 'takeuchi-daiki-20161130'

# CloudSQL & SQLAlchemy configuration
HOST = 'localhost'
PORT = '3306'
USER = 'test_user'
PASSWORD = 'test_user'
DATABASE = 'sample_db'
SQLALCHEMY_DATABASE_URI = (
    'mysql://{user}:{password}@{host}:{port}/{database}').format(
        user=USER, password=PASSWORD, host=HOST, port=PORT, database=DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = True

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'development key'

# Google Cloud Storage and upload settings.
CLOUD_STORAGE_BUCKET = 'takeuchi-20161130'
MAX_CONTENT_LENGTH = 8 * 1024 * 1024
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
