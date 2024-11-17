from flask import Flask, render_template, request, redirect, url_for, session
from database.db import (
    init_db,
    get_user_by_identifier,
    create_user,
    verify_user,
    register_user,
    get_all_posts,
    get_post,
    add_post,
    add_comment,
)

app = Flask(__name__)
app.secret_key = "super_secret_key"
init_db()


@app.before_request
def before_request():
    if (
        "user_identifier" not in session
        and request.endpoint != "login"
        and request.endpoint != "register"
    ):
        # Redirect to login if no identifier and not accessing login or register
        return redirect(url_for("login"))


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if verify_user(session["user_identifier"], username, password):
            return redirect(url_for("task"))
        else:
            return "Login Failed"
    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user_identifier = session.get("user_identifier")
        if register_user(user_identifier, username, password):
            return redirect(url_for("login"))
        else:
            return "Registration Failed"
    return render_template("register.html")


@app.route("/task")
def task():
    user = get_user_by_identifier(session["user_identifier"])
    if not user["authenticated"]:
        return redirect(url_for("login"))

    if not user["authorized"]:
        return "Unauthorized"

    return render_template(
        "task.html", task_message="You are authorized to perform this task."
    )


if __name__ == "__main__":
    app.run(debug=True)
