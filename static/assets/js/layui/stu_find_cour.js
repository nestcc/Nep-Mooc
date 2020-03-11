var onclick_id = 0;
var csrf_token = $('input:hidden').val();

layui.use(['laypage', 'layer'], function () {
    var laypage = layui.laypage;
    var layer = layui.layer;

    laypage.render({
        elem: 'lay-page',
        count: $('#item_number').html(),
        curr: location.href.split('/')[5],
        limit: 6,
        jump: function(obj, first){
            console.log(obj.curr);
            if (!first){
                location.href = '/student/search_course/' + obj.curr + '/';
            }
        }
    })
});

function view_info(id) {
    onclick_id = id;
    $.ajax({
        url: "/student/show_cour_info/" + id + "/",
        type: "GET",
        cache: false,
        success: function (data) {
            console.log(data);
            var layer = layui.layer;
            layer.open({
                type: 1,
                area: ["500px", "300px"],
                title: data['cour_name'],
                content: "<p>" + data['cour_type'] + "</p>" +
                    "<p>" + data['cour_schedule'] + "</p>" +
                    "<p>" + data['cour_description'] + "</p>" +
                    "<p>" + data['cour_tch'] + "</p>",

                btn: ['我要参加'],
                btn1: confirm,
            })
        }
    })
}


function confirm(index, layero) {
    $.ajax({
        url: '/student/join_course/',
        type: 'POST',
        cache: false,
        data: 'csrfmiddlewaretoken=' + csrf_token + '&id_cour=' + onclick_id,
        success: function (data) {
            if (data['status'] === 'SUCCESS') {
                layer.msg('OK!!!', {
                    time: 0,
                    btn: ['confirm']
                })
            } else if (data['status'] === 'FAIL' && data['error'] === 'DUAL') {
                layer.msg('你已经参加过了，无法重复参加', {
                    time: 0,
                    btn: ['confirm']
                })
            }
        }
    })
}