layui.use(['form', 'element', 'laydate'], function () {
    var form = layui.form;
    var laydate = layui.laydate;

    //日期
    laydate.render({
        elem: '#cour_range',
        type: 'datetime',
        range: true
    });
    var element = layui.element; //导航的hover效果、二级菜单等功能，需要依赖element模块

    //监听导航点击
    element.on('nav(demo)', function (elem) {
        //console.log(elem)
        layer.msg(elem.text());
    });


    form.on('submit(submit_btn)', function () {
        //
        // console.log(form.val("cour_form"));

        $.ajax({
            url: '/teacher/submit_course/',
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
                            console.log(data)
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
                // console.log(xhr);
            }
        });
        return false;
    })

});

