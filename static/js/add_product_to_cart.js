function addProductForm() {
    const selectedProduct = document.querySelector('input[name="color"]:checked').value;

    const count = document.querySelector('#product-count').value;

    const csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    const data = {
        product: selectedProduct,
        count: count
    };

    const messages = document.getElementById('messages-block');

    fetch('/orders/add_product_to_cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data),
    })
        .then(
            response => response.text())
}