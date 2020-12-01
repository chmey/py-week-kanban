class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_SETTINGS = {
        'db': 'kanweek',
        'host': 'db',
        'port': 27017
    }


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'kanweek',
        'host': 'localhost',
        'port': 27017
    }


class TestingConfig(Config):
    TESTING = True
