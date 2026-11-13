from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder="templates")

database_products = {
    "laptop": 180,
    "keyboard": 9
}


@app.route("/")
def main():
    return render_template("main.html")


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/add-product", methods=["POST"])
def add_product():
    product_name = request.form.get("products", "").strip()
    price_raw = request.form.get("price", "")

    try:
        if not product_name:
            raise ValueError("Product name cannot be empty.")

        price = float(price_raw)
        if price < 0:
            raise ValueError("Price cannot be negative.")

        database_products[product_name] = price
        return redirect("/users")

    except ValueError as e:
        return f"Error: {e}", 400


@app.route("/users")
def users():
    return render_template("users.html", products=database_products)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
