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
                        location.href=data['url'];
                    }
                })
            }
        })
    });

