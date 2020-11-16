class Config(object):
    DEBUG = False
    TESTING = False
    MONGOALCHEMY_DATABASE = 'kanweek'
    MONGOALCHEMY_SERVER = 'db'
    MONGOALCHEMY_PORT = 27017


class ProductionConfig(Config):
    DEBUG = False
    MONGOALCHEMY_SAFE_SESSION = True


class DevelopmentConfig(Config):
    DEBUG = True
    MONGOALCHEMY_SERVER = 'localhost'


class TestingConfig(Config):
    TESTING = True
