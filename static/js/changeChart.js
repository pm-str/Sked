$('.btn-group > a').click(function (e){
    e.preventDefault();
    $.ajax({
        type: "GET",
        url: "/home/api/chart",
        data: {
            'number': $(this).attr('data-v')
        },
        dataType: "HTML",
        cache: false,
        statusCode: {
            200: function () {
                location.reload();
            },
            401: function () {
                alert('An error occurred downloading');
            }
        }
    });
});