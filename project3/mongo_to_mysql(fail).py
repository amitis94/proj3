# GCS
## 클라우드 서버에 SQL 데이터베이스를 만듦
### 참고사이트: https://towardsdatascience.com/sql-on-the-cloud-with-python-c08a30807661

import mysql.connector
from mysql.connector.constants import ClientFlag
from pymongo import MongoClient

config = {
    'user': 'root',
    'password': 'rksk4137',
    'host': '34.64.103.116',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem'
}

# MySQL 인스턴스에 movieDB 생성
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()  # initialize connection cursor
#cursor.execute('CREATE DATABASE movieDB') 
#config['database'] = 'movieDB'  # add new database to config dict
cnxn.close()

# MongoDB 연결
URI = 'mongodb+srv://amitis:rksk4137@cluster.etbe6rl.mongodb.net/?retryWrites=true&w=majority'
client = MongoClient(URI)
DATABASE = 'MovieDB'
mong0_data = client[DATABASE]