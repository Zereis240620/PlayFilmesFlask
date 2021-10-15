import os
DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
TEMPLATES_AUTO_RELOAD = True
SECRET_KEY = 'encripitar-form'
UPLOAD_FOLDER = os.path.join(os.getcwd(),"app\\static\\uploads\\")