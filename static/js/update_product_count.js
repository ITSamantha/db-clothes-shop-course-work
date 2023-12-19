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
    var total = (parseFloat(newVal) * parseFloat(productPrice)).toFixed(1);
    productTotalTd.innerHTML = `<input type="hidden" value="${total}" id="product-total-val-${productId}">${total}$`

    updateSubtotalAmount();
    updateTotalAmount();


    const csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    const data = {
        product: productId,
        count: productCount.value,
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


document.addEventListener('DOMContentLoaded', updateSubtotalAmount());
document.addEventListener('DOMContentLoaded', updateTotalAmount());


function updateSubtotalAmount() {

    const productRows = document.querySelectorAll('.table tbody tr');

    let totalAmount = 0;

    productRows.forEach(row => {
        var priceInput = row.querySelector('[id^="product-total-val-"]')
        const sum = parseFloat(priceInput.value);
        totalAmount += sum;
    });

    document.getElementById('total-amount').textContent = totalAmount.toFixed(2) + '$';
    document.getElementById('total-amount-price').value = totalAmount.toFixed(2);
}

function updateTotalAmount() {
    const totalPrice = parseFloat(document.getElementById('total-amount-price').value)
    const totalShipping = parseFloat(document.getElementById('total-shipping-price').value)

    let totalAmount = totalPrice + totalShipping

    document.getElementById('total-order-price').textContent = totalAmount.toFixed(1) + '$';
}
