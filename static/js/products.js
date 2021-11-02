// window.onload = function prod(){
$('#item_list').ready(function () {
    $('#item_list').on('click', function () {
        let t_href = event.target;
        $.ajax({
            url: '/products/add/' + t_href.name + '/',
            success: function (data) {
                // $('#item_list').html(data.result);
            }
        })
    });
})
// }