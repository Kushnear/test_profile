import databases
import ormar
import sqlalchemy


HOST = 'db-profile'
PORT = 5432
POSTGRES_USER = 'uvicornuser'
POSTGRES_PASSWORD = '12345678'
POSTGRES_DB = 'profile'

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{HOST}:{PORT}/{POSTGRES_DB}"

metadata = sqlalchemy.MetaData()
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(DATABASE_URL)


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
