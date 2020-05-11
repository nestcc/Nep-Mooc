$.ajax({
    url: '/student/get_learned_sect/',
    type: 'POST',
    cache: false,
    data: {
        'csrfmiddlewaretoken': function () {
            return $('input:hidden').val()
        },
        'cour_id': self.location.href.split('/')[5]
    },
    success: function (data) {
        console.log(data);
        for (each_complete in data['complete']) {
            $('#header_' + data['complete'][each_complete]).removeClass('layui-bg-gray');
            $('#header_' + data['complete'][each_complete]).addClass('layui-bg-green');
        }
        for (each_start in data['start']) {
            $('#header_' + data['start'][each_start]).removeClass('layui-bg-gray');
            $('#header_' + data['start'][each_start]).addClass('layui-bg-cyan');
        }
    }
});

function learn(sect_id) {
    location.href = '/student/learn/' + sect_id + '/';
}

function quit(cour_id) {
    var csrf_token = $('input[name=csrfmiddlewaretoken]').val();
    $.ajax({
        url: '/student/quit_course/',
        type: 'POST',
        cache: false,
        data: {
            'csrfmiddlewaretoken': csrf_token,
            'cour_id': cour_id
        },
        success: function (data) {
            console.log(data);
            if (data['status'] === 'SUCCESS') {
                layer.msg('OK!!!', {
                    time: 3000,
                    closeBtn: 1,
                    end: function () {
                        location.href = '/student/my_course/1/';
                    }
                })
            } else {
                layer.msg(data['error'], {
                    time: 3000,
                    closeBtn: 1
                })
            }
        }
    });
}