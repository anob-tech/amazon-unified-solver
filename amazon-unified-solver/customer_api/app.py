from flask import Flask, jsonify

app = Flask(__name__)

products = {
    "laptop": {"price": 1200, "rating": 4.5},
    "phone": {"price": 800, "rating": 4.2},
    "headphones": {"price": 150, "rating": 4.0}
}

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Amazon Unified Solver - Customer API",
        "endpoints": {
            "/products": "List all products",
            "/recommend/<product>": "Get recommendation based on product"
        }
    })

@app.route('/products')
def list_products():
    return jsonify(products)

@app.route('/recommend/<product>')
def recommend(product):
    product = product.lower()
    if product in products:
        return jsonify({
            "recommendation": f"If you like {product}, you may also like headphones 🎧"
        })
    else:
        return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
