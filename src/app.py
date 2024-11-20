from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from database.db import (
    init_db,
    get_all_products,
    get_product_by_id,
    get_user_by_username,
)
import uuid

app = Flask(__name__)
app.secret_key = "super_secret_key"
init_db()

users = {
    "authorized_user": {"password": "password123", "authorized": True},
    "unauthorized_user": {"password": "password123", "authorized": False},
}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        print(
            f"Accessing {request.path} by {session['username']}. Session: {session}"
        )  # Print session details
        return f(*args, **kwargs)

    return decorated_function


@app.before_request
def before_request():
    if not session.get("session_id"):
        session["session_id"] = str(uuid.uuid4())
    if "cart" not in session:
        session["cart"] = []
    print(
        f"Session before request: {session}"
    )  # Print session details before each request


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/products")
@login_required
def products():
    products = get_all_products()
    return render_template("products.html", products=products)


@app.route("/add_to_cart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    product = get_product_by_id(product_id)
    if product:
        cart = session.get("cart", [])
        for item in cart:
            if item["id"] == product[0]:
                item["quantity"] += 1
                session["cart"] = cart
                print(
                    f"Updated session (add to cart): {session}"
                )  # Print session details
                return jsonify(success=True)
        cart.append(
            {"id": product[0], "title": product[1], "price": product[2], "quantity": 1}
        )
        session["cart"] = cart
        print(f"Updated session (add to cart): {session}")  # Print session details
        return jsonify(success=True)
    return jsonify(success=False)


@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    if request.method == "POST":
        cart = session.get("cart", [])
        updated_cart = []
        for item in cart:
            item_id = str(item["id"])
            quantity_field = f"quantity_{item_id}"
            if quantity_field in request.form:
                try:
                    quantity = int(request.form[quantity_field])
                    if quantity > 0:
                        item["quantity"] = quantity
                        updated_cart.append(item)
                    elif quantity == 0:
                        print(
                            f"Removing item ID {item_id} from cart as quantity is zero."
                        )
                    else:
                        print(
                            f"Invalid quantity for item ID {item_id}. Skipping update."
                        )
                except ValueError:
                    print(
                        f"Invalid quantity value for item ID {item_id}. Skipping update."
                    )
            else:
                updated_cart.append(item)
        session["cart"] = updated_cart
        print(f"Updated session (cart): {session}")  # Print session details

    cart = session.get("cart", [])
    total_amount = sum(item.get("price", 0) * item.get("quantity", 0) for item in cart)
    return render_template("cart.html", cart=cart, total_amount=total_amount)


@app.route("/checkout", methods=["GET", "POST"])
@login_required
def checkout():
    user = users.get(session["username"])

    if user and user["authorized"]:
        cart = session.get("cart", [])
        total_amount = sum(
            item.get("price", 0) * item.get("quantity", 0) for item in cart
        )

        if request.method == "POST":
            session["cart"] = []
            print(f"Updated session (checkout): {session}")  # Print session details
            return render_template(
                "checkout.html",
                message="Order placed successfully!",
                total_amount=total_amount,
            )

        return render_template("checkout.html", total_amount=total_amount)
    else:
        # Unauthorized access attempt
        print(
            f"Unauthorized checkout attempt by {session['username']}. Session: {session}"
        )
        return render_template(
            "error.html", message="You are not authorized to perform this operation."
        )


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = users.get(username)

        if user:
            print(f"User {username} found. Checking password...")
        else:
            print(f"User {username} not found.")

        if user and user["password"] == password:
            session.clear()  # Clear existing session
            session["username"] = username
            session["session_id"] = str(uuid.uuid4())  # Generate a new session ID
            print(f"User {username} logged in. New Session: {session}")
            return redirect(url_for("products"))
        else:
            print("Invalid username or password.")
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")


@app.route("/logout")
def logout():
    print(
        f"User {session.get('username')} logging out. Session: {session}"
    )  # Print session details before logout
    session.clear()  # Clear the entire session
    return redirect(url_for("login"))


@app.route("/task", methods=["GET", "POST"])
@login_required
def task():
    user = users.get(session["username"])
    if user and user["authorized"]:
        if request.method == "POST":
            print(
                f"Task performed by {session['username']}. Session: {session}"
            )  # Print session details
            return render_template("task.html", message="Task performed successfully!")
        return render_template("task.html")
    else:
        print(
            f"Unauthorized task access by {session['username']}. Session: {session}"
        )  # Print session details
        return render_template("task.html", error="Unauthorized to perform this task")


@app.route("/cart_count")
def cart_count():
    cart = session.get("cart", [])
    count = sum(item.get("quantity", 0) for item in cart)
    return jsonify(success=True, count=count)


if __name__ == "__main__":
    app.run(debug=True)
