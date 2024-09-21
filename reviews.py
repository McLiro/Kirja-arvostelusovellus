from db import db
import users

def get_list():
    sql = "SELECT R.title, R.score, U.username, R.sent_at FROM reviews R, users U WHERE R.user_id=U.id ORDER BY R.id"
    result = db.session.execute(sql)
    return result.fetchall()