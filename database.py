import sqlite3
from werkzeug.security import generate_password_hash
from flask import current_app

def get_db_connection():
    """Get database connection with row factory"""
    conn = sqlite3.connect(current_app.config['DATABASE_PATH'])
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables and create default user"""
    conn = get_db_connection()
    c = conn.cursor()
    
    # Create users table
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  username TEXT UNIQUE NOT NULL,
                  password_hash TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # Create tasks table
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  status TEXT NOT NULL DEFAULT 'pending',
                  priority TEXT NOT NULL DEFAULT 'medium',
                  is_urgent BOOLEAN NOT NULL DEFAULT 0,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                  user_id INTEGER,
                  FOREIGN KEY (user_id) REFERENCES users (id))''')
    
    # Create default user if not exists
    c.execute("SELECT * FROM users WHERE username = ?", ('admin',))
    if not c.fetchone():
        password_hash = generate_password_hash('admin123')
        c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", 
                 ('admin', password_hash))
    
    conn.commit()
    conn.close()

def execute_query(query, params=None, fetch_one=False, fetch_all=False):
    """Execute database query with proper connection handling"""
    conn = get_db_connection()
    try:
        if params:
            result = conn.execute(query, params)
        else:
            result = conn.execute(query)
        
        if fetch_one:
            return result.fetchone()
        elif fetch_all:
            return result.fetchall()
        else:
            conn.commit()
            return result.lastrowid
    finally:
        conn.close()
