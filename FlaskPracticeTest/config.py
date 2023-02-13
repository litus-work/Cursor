
class Config:
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = 'litus_cursor'
    PG_PASSWORD = '0791LitusCursor'
    PG_HOST = '127.0.0.1'
    PG_PORT = 5432
    DB_NAME = 'cursor_db'
    DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = 'litus_cursor'
    PG_PASSWORD = '0791LitusCursor'
    PG_HOST = '127.0.0.1'
    PG_PORT = 5432
    DB_NAME = 'test_cursor_db'
    DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def get_config(env="DEV"):
    if env == "TEST":
        return TestConfig
    return Config
