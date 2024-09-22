from db import db
import users
from sqlalchemy.sql import text

def get_list():
    sql = "SELECT R.title, R.score, U.username, R.sent_at FROM reviews R, users U WHERE R.user_id=U.id ORDER BY R.id"
    result = db.session.execute(text(sql))
    return result.fetchall()

def new_review(title, content, score):
    user_id = users.user_id()
    if user_id == 0:
        return False
    sql = "INSERT INTO reviews (title, content, score, user_id, sent_at) VALUES (:title, :content, :score, :user_id, NOW()) RETURNING id"
    result = db.session.execute(text(sql), {"title":title, "content":content, "score":score, "user_id":user_id})
    db.session.commit()
    return result.fetchone[0]