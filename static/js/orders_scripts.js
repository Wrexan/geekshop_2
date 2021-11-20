window.onload = function () {
    let _quantity, _price, orderitem_num, delta_quantity, orderitem_quantity, delta_cost;
    let quantity_arr = [];
    let price_arr = [];

    let total_forms = parseInt($('input[name="orderitems-TOTAL_FORMS"]').val());

    let order_total_quantity = parseInt($('.order_total_quantity').text()) || 0;
    let order_total_price = parseFloat($('.order_total_cost').text().replace(',', '.'));

    for(let i=0; i<total_forms; i++){
        _quantity = parseInt($('input[name="orderitems-' + i + '-quantity"]').val());
        _price = parseFloat($('.orderitems-' + i + '-price').val().replace(',', '.'));
    }
}