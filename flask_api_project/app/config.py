# app/config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Vero2402*@localhost/flask_api_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
