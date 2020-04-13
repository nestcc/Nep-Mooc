$('#submit_btn').click(function () {
    if (location.href.split('/')[4] === 'stu_login') {
        var submit_url = '/index/submit_stu_login/';
        var end_url = '/student/index/';
    } else {
        var submit_url = '/index/submit_tch_login/';
        var end_url = '/teacher/index/';
    }

    $.ajax({
        url: submit_url,
        type: 'POST',
        data: $("#user_login").serialize(),
        cache: false,
        success: function (data) {
            if (data['status'] === 'SUCCESS') {
                layer.msg('OK!!!', {
                    time: 3000,
                    closeBtn: 1,
                    end: function () {
                        location.href = end_url;
                    }
                });
            } else {
                layer.msg('信息错误', {
                    time: 3000,
                    closeBtn: 1
                })
            }

        }
    })
});