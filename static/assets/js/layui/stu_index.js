layui.use(['carousel'], function () {
    var carousel = layui.carousel;
    carousel.render({
        elem: '#index_carousel',
        width: '100%',
        height: '450px',
        arrow: 'always',
    });
});

function get_recommend() {
    console.log('onclick');
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url: '/student/get_recommend/',
        type: 'POST',
        cache: false,
        data: {'csrfmiddlewaretoken': csrf_token},
        success: function (data) {
            console.log(data['value']);
            layer.msg(data['value'].toString(), {
                time: 3000,
                closeBtn: 1
            })
        }
    })
}