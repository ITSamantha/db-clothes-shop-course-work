function updateTotalAmount(isShipping) {
    let totalPrice = parseFloat(document.getElementById('total-amount-price').value)
    if (isShipping) {
        const totalShipping = parseFloat(document.getElementById('total-shipping-price').value)
        totalPrice += totalShipping
    }
    document.getElementById('total-order-price').textContent = totalPrice.toFixed(1) + '$';
}

document.addEventListener('DOMContentLoaded', function () {
    var hasShippingPrice = !!document.getElementById('total-shipping-price');
    updateTotalAmount(hasShippingPrice);
});