$(document).ready(function () {
    getSize();
    console.log('yes')

    $(document).on('change', 'form#size-form input[type="radio"]', getSize);

});

function getSize() {

    var formData = $('#size-form').serialize();

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