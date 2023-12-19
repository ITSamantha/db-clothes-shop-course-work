function removeProductFromCart(event) {
    var button = event.target;

    const cartId = parseInt(button.id);


    if (button.classList.contains('remove')) {
        const cartTr = document.querySelector(`tr[id="${cartId}"]`)

        cartTr.remove()
        const csrfToken = $('[name="csrfmiddlewaretoken"]').val();

        const data = {
            cart: cartId,
        };

        fetch('/orders/remove_product_from_cart/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify(data),
        }).then(r => r)
    }

}

