document.addEventListener('DOMContentLoaded', () => {
    fetch('http://localhost:5000/api/products')
        .then(response => response.json())
        .then(products => {
            const container = document.getElementById('products');
            products.forEach(product => {
                const productDiv = document.createElement('div');
                productDiv.className = 'product';
                productDiv.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Price: $${product.price}</p>
                    <p>Stock: ${product.stock}</p>
                    <button onclick="placeOrder(${product.id})">Buy Now</button>
                `;
                container.appendChild(productDiv);
            });
        });
});

function placeOrder(productId) {
    fetch('http://localhost:5000/api/order', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ product_id: productId, quantity: 1 })
    })
    .then(response => response.json())
    .then(data => alert(data.success || data.error))
    .catch(error => alert('Error placing order'));
}
