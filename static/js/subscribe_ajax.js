$(document).ready(function () {

    showSubscribeForm();

    $(document).on('submit', 'form#subscribe-form', function (event) {
        event.preventDefault();
        submitSubscribeForm();
    });
});


function showSubscribeForm() {
    $.ajax({
        type: 'GET',
        url: '/users/subscribe/',
        success: function (response) {
            $('#subscribe-col').html(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
}

function submitSubscribeForm() {

    var formData = $('#subscribe-form').serialize();

    var csrfToken = $('[name="csrfmiddlewaretoken"]').val();

    console.log(formData)
    $.ajax({
        type: 'POST',
        url: '/users/subscribe/',
        headers: {
            'X-CSRFToken': csrfToken
        },
        data: formData,
        success: function (response) {
            $('#subscribe-col').html(response);
        },
        error: function (error) {
            console.log(error);
        }
    });
}