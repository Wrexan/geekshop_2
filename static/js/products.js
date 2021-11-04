// window.onload = function prod(){
$('#item_list').ready(function () {
    $('#item_list').on('click', function () {
        let t_href = event.target;
        console.log(t_href.name);
        $.ajax({
            url: '/products/add/' + t_href.name + '/',
            success: function (data) {
                // $('#baskq').html(data.result);
                // console.log(data.result);
            }
        });
    });
});
// }