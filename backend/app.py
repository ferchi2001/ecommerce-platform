from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 999.99, "stock": 10},
    {"id": 2, "name": "Smartphone", "price": 699.99, "stock": 15},
    {"id": 3, "name": "Headphones", "price": 149.99, "stock": 20},
]

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify(products)

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

@app.route('/api/order', methods=['POST'])
def place_order():
    data = request.json
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    if product['stock'] < quantity:
        return jsonify({"error": "Insufficient stock"}), 400
    
    product['stock'] -= quantity
    return jsonify({"success": f"Order placed for {quantity} {product['name']}(s)"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
