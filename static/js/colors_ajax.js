$(document).ready(function () {
    getColor();
    $(document).on('change', 'form#color-form input[type="radio"]', getColor);

});

function getColor() {

    var formData = $('#color-form').serialize();

    var product_id = $('#product').val();

    console.log(formData)
    $.ajax({
        type: 'GET',
        url: product_id + '/size_details/',
        data: formData,
        success: function (response) {
            $('#product-detail-sizes-colors').html(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
}