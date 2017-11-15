class BaseConfig(object):
    "配置基类"
    SECRET_KEY = 'makesure to set a very secret key'


class DevelopmentConfig(BaseConfig):
    "开发环境配置"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    "生产环境配置"
    pass


class TestingConfig(BaseConfig):
    "测试环境配置"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root:root@localhost:3306/jobplus?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


configs = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
        }

