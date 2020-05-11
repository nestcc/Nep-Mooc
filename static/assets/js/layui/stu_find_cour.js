var csrf_token = $('input:hidden').val();

layui.use(['laypage', 'layer', 'form'], function () {
    var laypage = layui.laypage;
    var layer = layui.layer;
    var form = layui.form;

    laypage.render({
        elem: 'lay-page',
        count: $('#item_number').html(),
        curr: location.href.split('/')[5],
        limit: 6,
        jump: function (obj, first) {
            if (!first) {
                var url_spliter = location.href.split('/');
                if (url_spliter.length === 7) {
                    location.href = '/student/search_course/' + obj.curr + '/';
                } else {
                    location.href = '/student/search_course/' + obj.curr + '/' + url_spliter[6] + '/';
                }
            }
        }
    });

});

function get_recommend() {
    layer.open({
        title: '推荐课程',
        type: 2,
        shade: false,
        area: '320px',
        maxmin: true,
        content: '/student/get_recommend/',
        closeBtn: 1,
    });
}

function view_info(id) {
    layer.open({
        title: '课程详情',
        type: 2,
        shade: false,
        area: ['1000px', '500px'],
        maxmin: true,
        content: '/student/show_cour_detail/' + id + '/',
        btn: ['参加课程'],
        btn1: function (index, layero) {
            confirm(id)
        }
    });
}


function confirm(id) {
    $.ajax({
        url: '/student/join_course/',
        type: 'POST',
        cache: false,
        data: 'csrfmiddlewaretoken=' + csrf_token + '&id_cour=' + id,
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

function search_by_info(text) {
    if (text === '') {
        location.href = '/student/search_course/1/';
    } else {
        location.href = '/student/search_course/1/' + text + '/';
    }
}