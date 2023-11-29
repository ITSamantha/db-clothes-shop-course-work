$(document).on('change', 'form#filter-form input[type="checkbox"]', function () {

    var formData = $('#filter-form').serialize();
    console.log('FormData:', formData);

    $.ajax({
        type: 'GET',
        url: '/products/filter_products/',
        data: formData,
        success: function (response) {
            $('#products-container').html(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
});
