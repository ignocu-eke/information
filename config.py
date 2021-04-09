from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG = True

    SECRET_KEY = 'RSKJscHPom4tos+pnx8cQc6ZZMfIIedXXqdvL77SEWQRKRnUBPq0fSM65la1D3hS'
    # 为Mysql　数据库添加配置
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information27'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 为redis 的配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # Session 保存设置
    SESSION_TYPE = 'redis'
    # 开启 Session 签名
    SESSION_USE_SIGNER = True
    # 指定 Session　保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
