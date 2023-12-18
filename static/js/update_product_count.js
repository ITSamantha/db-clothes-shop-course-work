function updateProductCount(event) {
    var button = event.target;

    const productId = document.querySelector('#product-id-' + parseInt(button.id)).value;

    const productCount = document.querySelector('#product-count-' + productId);


    var oldValue = parseInt(productCount.value);


    if (button.classList.contains('plus')) {
        var newVal = parseFloat(oldValue) + 1;
    } else {
        if (oldValue > 0) {
            var newVal = parseFloat(oldValue) - 1;
        } else {
            newVal = 0;
        }
    }

    if (newVal > parseInt(productCount.max)) {
        return;
    }

    productCount.value = newVal;

    const productPrice = document.querySelector('#product-price-' + productId).value;

    var productTotalTd = document.querySelector('#product-total-' + productId)
    productTotalTd.textContent = (parseFloat(newVal) * parseFloat(productPrice)).toFixed(1) + '$';

    const csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    const data = {
        product: productId,
        count: productCount,
    };

    fetch('/orders/update_product_count_in_cart/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify(data),
    }).then(r => r)
}