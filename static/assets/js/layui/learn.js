document.getElementById('sect_video').addEventListener('ended',
    function () {
        $.ajax({
            url: '/student/finished/',
            type: 'POST',
            cache: false,
            data: {
                'csrfmiddlewaretoken': function () {
                    return $('input:hidden').val()
                },
                'sect_id': self.location.href.split('/')[5]
            },
            success: function (data) {
                layer.msg('学习完这一课了！', {
                    time: 3000,
                    btn: ['返回列表'],
                    end: function () {
                        location.href = data['url'];
                    }
                })
            }
        })
    });

layui.use(['util'], function () {
    var util = layui.util,
        layer = layui.layer;
    var cour_id = $('input[name=cour_id]').val();
    //固定块
    util.fixbar({
        bar1: '&#xe65c',
        css: {right: 50, bottom: 50},
        bgcolor: '#9F9F9F',
        click: function (type) {
            if (type === 'bar1') {
                location.href = '/student/course_page/' + cour_id + '/';
            }
        }
    });
});

