from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from database.db import (
    init_db,
    get_all_products,
    get_product_by_id,
    get_user_by_username,
)

app = Flask(__name__)
app.secret_key = "super_secret_key"
init_db()

users = {
    "authorized_user": {"password": "password123", "authorized": True},
    "unauthorized_user": {"password": "password123", "authorized": False},
    "non_existent_user": {
        "password": "password123",
        "authorized": False,
    },  # This user is not registered
}


@app.before_request
def before_request():
    if "cart" not in session:
        session["cart"] = []


@app.route("/")
def index():
    return redirect(url_for("products"))


@app.route("/products")
def products():
    products = get_all_products()
    return render_template("products.html", products=products)


@app.route("/add_to_cart/<int:product_id>")
def add_to_cart(product_id):
    if "username" not in session:
        return jsonify(success=False, message="User not authenticated")

    product = get_product_by_id(product_id)
    if product:
        cart = session.get("cart", [])
        for item in cart:
            if item["id"] == product[0]:
                item["quantity"] += 1
                session["cart"] = cart
                return jsonify(success=True)
        cart.append(
            {"id": product[0], "title": product[1], "price": product[2], "quantity": 1}
        )
        session["cart"] = cart
        return jsonify(success=True)
    return jsonify(success=False)


@app.route("/cart", methods=["GET", "POST"])
def cart():
    if "username" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        cart = session.get("cart", [])
        updated_cart = []
        for item in cart:
            item_id = str(item["id"])
            if item_id in request.form:
                quantity = int(request.form[item_id])
                if quantity > 0:
                    item["quantity"] = quantity
                    updated_cart.append(item)
        session["cart"] = updated_cart

    cart = session.get("cart", [])
    total_amount = sum(item["price"] * item["quantity"] for item in cart)
    return render_template("cart.html", cart=cart, total_amount=total_amount)


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    if "username" not in session:
        return redirect(url_for("login"))

    cart = session.get("cart", [])
    total_amount = sum(item["price"] * item["quantity"] for item in cart)

    if request.method == "POST":
        # Process the checkout (e.g., save order to the database, clear the cart)
        session["cart"] = []
        return render_template(
            "checkout.html",
            message="Order placed successfully!",
            total_amount=total_amount,
        )

    return render_template("checkout.html", total_amount=total_amount)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)

        if user and user["password"] == password:
            session["username"] = username
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))


@app.route("/task", methods=["GET", "POST"])
def task():
    if "username" not in session:
        return redirect(url_for("login"))

    user = users.get(session["username"])
    if user and user["authorized"]:
        if request.method == "POST":
            # Perform the task
            return render_template("task.html", message="Task performed successfully!")
        return render_template("task.html")
    else:
        return render_template("task.html", error="Unauthorized to perform this task")


if __name__ == "__main__":
    app.run(debug=True)
