function countSubtotal() {
    const productRows = document.querySelectorAll('.product');
    let subtotalAmount = 0;

    productRows.forEach(row => {
        const productSumElement = row.querySelector('input[type="hidden"]');
        const productSum = parseFloat(productSumElement.value);
        subtotalAmount += productSum;
    });

    document.getElementById('total-amount').textContent = subtotalAmount.toFixed(2) + '$';
    document.getElementById('total-amount-price').value = subtotalAmount.toFixed(2);
}

document.addEventListener('DOMContentLoaded', countSubtotal());