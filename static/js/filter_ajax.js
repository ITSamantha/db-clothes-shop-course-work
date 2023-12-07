$(document).ready(function () {

    handleFilterChange();
    $(document).on('change', 'form#filter-form input[type="checkbox"]', handleFilterChange);
});

function handleFilterChange() {
    var formData = $('#filter-form').serialize();
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
}


