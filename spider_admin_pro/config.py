# -*- coding: utf-8 -*-

# flask 服务配置
FLASK_PORT = 5001
FLASK_HOST = '127.0.0.1'

# scrapyd地址
SCRAPYD_SERVER = 'http://127.0.0.1:6800'

# 登录账号密码
BASIC_AUTH_USERNAME = "admin"
BASIC_AUTH_PASSWORD = "123456"
BASIC_AUTH_JWT_KEY = "ooxx"

# 调度历史存储设置 mysql or sqlite
SCHEDULE_DATABASE_SCHEME = 'sqlite'
SCHEDULE_DATABASE_NAME = 'history.db'
SCHEDULE_DATABASE_USER = 'root'
SCHEDULE_DATABASE_PASSWORD = '123456'
SCHEDULE_DATABASE_HOST = 'localhost'
SCHEDULE_DATABASE_PORT = 3306