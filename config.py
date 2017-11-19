import os
basedir = os.path.abspath(os.path.dirname(__file__))

# path of database file
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

# folder where we will store SQLAlchemy-migrate data files.
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

SQLALCHEMY_TRACK_MODIFICATIONS = False