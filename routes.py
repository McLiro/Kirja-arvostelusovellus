from app import app
from flask import render_template, request, redirect, url_for
import reviews, users

@app.route("/")
def index():
    if "user_id" in users.session:
        list = reviews.get_list()
        return render_template("index.html", reviews=list)
    else:
        return redirect("/login")

@app.route("/new")
def new():
    return render_template("new.html")

@app.route("/create", methods=["POST"])
def create():
    title = request.form["title"]
    content = request.form["content"]
    score = request.form["score"]
    id = reviews.new_review(title, content, score)
    return redirect(url_for("review", id=id))

@app.route("/review/<int:id>")
def review(id):
    review = reviews.get_review(id)[0]
    title = review[0]
    content = review[1]
    score = review[2]
    sent_at = review[3]
    username = review[4]
    return render_template("review.html", title=title, content=content, score=score, sent_at=sent_at, username=username)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Väärä tunnus tai salasana.")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Rekisteröinti ei onnistunut.")
        
@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")