import os


class Config:
    TEST_VALUE = "CONFIG_VALUE"
    SECRET_KEY = b'\x08\x0e_\xb8\x94]\xacL\x13N\xedVD\xba\xfd\x85'
    PG_USER = 'litus_cursor'
    PG_PASSWORD = '0791LitusCursor'
    PG_HOST = '127.0.0.1'
    PG_PORT = 5432
    DB_NAME = 'cursor_db'
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False




class DevConfig(Config):
    TEST_VALUE = "DEV_CONFIG_VALUE"


class TestConfig(Config):
    TEST_VALUE = "TEST_CONFIG_VALUE"


def run_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    elif env == "TEST":
        return TestConfig
    else:
        return Config