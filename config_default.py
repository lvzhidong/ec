
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:A6809403b!@127.0.0.1:3306/test?charset=utf8'
    SECRET_KEY = '@#vsadsf$%tw$sdfaWETWAEF#A3DET2SDF'
    BABEL_DEFAULT_LOCALE = 'zh_CN'
    SSO_APP = 'sample'
    LOGIN_NOTIFY_URL = 'http://127.0.0.1:5000/admin/notify/'
