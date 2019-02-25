import socket

MONGODB_HOST = 'mongo'
MONGODB_PORT = 27017

REDISHOST = 'redis'
REDISPORT = '6379'
REDISPWD = ""

DB_HOST = 'postgres'
DB_PORT = 5432
APP_NAME = 'hod'
DB_USER = 'postgres'
DB_PASSWORD = 'HODL!fe'
FLASK_HOST = '0.0.0.0'
MAXACTIONCOUNT = 10
MAXLEARNCOUNT = 10
MAXCAPTURECOUNT = 34
MAXHRA = 157

REFERRAL_BALANCE = 500
DOCTOR_CHANGE = 0
DOCTOR_TOTAL_ONLINE_COUNT = ""
DOCTOR_SUBCAT_ONLINE_COUNT = ""
DOCTRO_CHARGER_PERCENTAGE = 0
FLASK_PORT = 8089
current_url='http://reports.hod.life'
staging = False
SECRET_KEY = '7rpFopPJTCgOjeZ62eD9Uw=='

host_name = socket.gethostname()
FLASK_DEBUG = False

ALLOWED_IP = ['127.0.0.1','104.131.175.242','165.227.213.71','138.197.76.153']

if host_name != 'reports':
    FLASK_DEBUG = True
    FLASK_HOST = '0.0.0.0'
    FLASK_PORT = 8090
    APP_NAME = 'hod'
    DB_HOST = 'localhost'
    DB_PORT = 5432
    DB_USER = 'postgres'
    DB_PASSWORD = 'HODL!fe'
    MONGODB_HOST = 'mongo'
    MONGODB_PORT = 27017
    SECRET_KEY='QhmikixruZTceEVBNr1tRNt7CZY9TU9zhKFEqtu55cU='
    current_url = 'http://0.0.0.0:8089'



SQLALCHEMY_DATABASE_URI = 'postgresql://' + str(DB_USER) + ':' + str(DB_PASSWORD) + '@' + str(DB_HOST) + ":" + str(DB_PORT) + '/' + str(APP_NAME)
DB_CONNECTION = "host='{0}' port='{1}' dbname='{2}' user='{3}' password='{4}'".format(DB_HOST, DB_PORT, APP_NAME,
                                                                                      DB_USER, DB_PASSWORD)


