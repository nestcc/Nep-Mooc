layui.use(['form', 'element', 'laydate', 'upload'], function () {
    var form = layui.form;
    var laydate = layui.laydate;
    var lay_upload = layui.upload;


    //日期
    laydate.render({
        elem: '#cour_range',
        type: 'datetime',
        range: true
    });

    lay_upload.render({
        elem: '#upload_image',
        url: '/teacher/cour_image/',
        data: {
            'csrfmiddlewaretoken': function () {
                return $('input:hidden').val()
            },
            'type': 'image',
            'cour_id': $('#cour_id').val()
        },
        done: function (data) {
            if (data['status'] === 'SUCCESS'){
                layer.msg("OK!!!", {
                    time: 0,
                    btn: 'confirm',
                    end: function () {
                        window.location.reload()
                    }
                })
            }
        },
        error: function () {
            //请求异常回调
        }
    });

    form.on('switch(cour_available)', function (data) {
        // cour_available = !!console.log(data.elem.checked);
        // form.val("cour_form", {
        //     "cour_available": cour_available
        // })
        if (data.elem.checked) {
            document.getElementById("cour_available").setAttribute("value", "True");
        } else {
            document.getElementById("cour_available").setAttribute("value", "False");
        }

    });

    form.on('submit(submit_btn)', function () {
        //
        // console.log(form.val("cour_form"));

        $.ajax({
            url: '/teacher/update_course/',
            type: 'POST',
            data: $("#cour_form").serialize(),
            cache: false,
            success: function (data) {
                console.log(form.val("cour_form"));
                if (data['status'] === 'SUCCESS') {
                    layer.msg("OK!!!!", {
                        time: 0,
                        btn: ['confirm'],
                        end: function () {
                            location.reload();
                        }
                    });
                } else {
                    layer.msg(data['status'], {
                        time: 0,
                        btn: ['confirm']
                    })
                }
            },
            error: function (xhr) {
                layer.msg('发送数据时发送错误', {
                    time: 0,
                    btn: ['confirm']
                });
                console.log(xhr);
            }
        });
        return false;
    })

})
;

$('#add_section').click(function () {
    location.href = '/teacher/cour_section/' + document.getElementById('cour_id').value
        + '/' + document.getElementById('cour_name').value + '/';
});

$('#del').click(function () {
    $.ajax({
            url: '/teacher/delete_course/',
            type: 'POST',
            data: $("#cour_form").serialize(),
            cache: false,
            success: function (data) {
                // console.log(form.val("cour_form"));
                if (data['status'] === 'SUCCESS') {
                    layer.msg("OK!!!!", {
                        time: 0,
                        btn: ['confirm'],
                        end: function () {
                            location.href='/teacher/manage_course/';
                        }
                    });
                } else {
                    layer.msg(data['status'], {
                        time: 0,
                        btn: ['confirm']
                    })
                }
            },
            error: function (xhr) {
                layer.msg('发送数据时发送错误', {
                    time: 0,
                    btn: ['confirm']
                });
                console.log(xhr);
            }
        });
});