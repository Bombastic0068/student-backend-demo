from flask import Flask, jsonify, request

app = Flask(__name__)

# These lists are the application's only storage. They reset when the server restarts.
users = []
products = []
orders = []


def next_id(items):
    return len(items) + 1


@app.route("/users", methods=["GET", "POST"])
def users_resource():
    if request.method == "GET":
        return jsonify(users)

    data = request.get_json(silent=True) or {}
    name = data.get("name")
    email = data.get("email")
    if not name or not email:
        return jsonify({"error": "name and email are required"}), 400

    user = {"id": next_id(users), "name": name, "email": email}
    users.append(user)
    return jsonify(user), 201


@app.route("/products", methods=["GET", "POST"])
def products_resource():
    if request.method == "GET":
        return jsonify(products)

    data = request.get_json(silent=True) or {}
    name = data.get("name")
    price = data.get("price")
    if not name or not isinstance(price, (int, float)):
        return jsonify({"error": "name and numeric price are required"}), 400

    product = {"id": next_id(products), "name": name, "price": price}
    products.append(product)
    return jsonify(product), 201


@app.route("/orders", methods=["GET", "POST"])
def orders_resource():
    if request.method == "GET":
        return jsonify(orders)

    data = request.get_json(silent=True) or {}
    user_id = data.get("user_id")
    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not isinstance(quantity, int) or quantity < 1:
        return jsonify({"error": "quantity must be a positive integer"}), 400
    if not any(user["id"] == user_id for user in users):
        return jsonify({"error": "user_id does not exist"}), 400
    if not any(product["id"] == product_id for product in products):
        return jsonify({"error": "product_id does not exist"}), 400

    order = {
        "id": next_id(orders),
        "user_id": user_id,
        "product_id": product_id,
        "quantity": quantity,
    }
    orders.append(order)
    return jsonify(order), 201


if __name__ == "__main__":
    app.run(debug=True)
