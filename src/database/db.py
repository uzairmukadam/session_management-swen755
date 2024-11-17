import sqlite3
import os

DATABASE_PATH = os.path.join(
    os.path.dirname(__file__), "../../database/message_wall.db"
)


def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        """CREATE TABLE IF NOT EXISTS posts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS comments
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, post_id INTEGER, content TEXT,
                  FOREIGN KEY(post_id) REFERENCES posts(id))"""
    )
    c.execute(
        """CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, identifier TEXT, username TEXT, password TEXT, authenticated BOOLEAN, authorized BOOLEAN)"""
    )
    conn.commit()
    conn.close()


def create_user(identifier):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO users (identifier, authenticated, authorized) VALUES (?, ?, ?)",
        (identifier, False, False),
    )
    conn.commit()
    conn.close()


def get_user_by_identifier(identifier):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE identifier = ?", (identifier,))
    user = c.fetchone()
    conn.close()
    return {
        "id": user[0],
        "identifier": user[1],
        "username": user[2],
        "password": user[3],
        "authenticated": user[4],
        "authorized": user[5],
    }


def verify_user(identifier, username, password):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        "UPDATE users SET username = ?, password = ?, authenticated = ?, authorized = ? WHERE identifier = ?",
        (username, password, True, username == "authorized_user", identifier),
    )
    conn.commit()
    conn.close()
    return True


def register_user(identifier, username, password):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        "UPDATE users SET username = ?, password = ?, authenticated = ?, authorized = ? WHERE identifier = ?",
        (username, password, True, False, identifier),
    )
    conn.commit()
    conn.close()
    return True


def get_all_posts():
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM posts")
    posts = c.fetchall()
    conn.close()
    return posts


def get_post(post_id):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("SELECT * FROM posts WHERE id = ?", (post_id,))
    post = c.fetchone()
    c.execute("SELECT * FROM comments WHERE post_id = ?", (post_id,))
    comments = c.fetchall()
    conn.close()
    return {"post": post, "comments": comments}


def add_post(title, content):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()


def add_comment(post_id, content):
    conn = sqlite3.connect(DATABASE_PATH)
    c = conn.cursor()
    c.execute(
        "INSERT INTO comments (post_id, content) VALUES (?, ?)", (post_id, content)
    )
    conn.commit()
    conn.close()
