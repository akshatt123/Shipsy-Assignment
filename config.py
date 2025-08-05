import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')
    DATABASE_PATH = os.environ.get('DATABASE_PATH', 'tasks.db')
    ITEMS_PER_PAGE = int(os.environ.get('ITEMS_PER_PAGE', '5'))
    
class DevelopmentConfig(Config):
    DEBUG = True
    
class ProductionConfig(Config):
    DEBUG = False
