tinymce.init({
    selector: '#sect_text',
    // inline: true,
    menubar: false,
    height: 400,
    language: 'zh_CN'
});

var url_param = '';

layui.use(['form', 'upload'], function () {
    var form = layui.form;
    var upload = layui.upload;
    var sect_cour = self.location.href.split('/')[5];
    url_param = '&sect_cour=' + sect_cour;

    upload.render({
        elem: '#upload_btn',
        url: '/teacher/upload/',
        accept: 'file',
        exts: 'mp4',
        size: 512000,
        data: {
            'csrfmiddlewaretoken': function () {
                return $('input:hidden').val()
            },
            'type': 'video',
            'cour_id': sect_cour,
            'tag': function () {
                return $('#sect_tag').val();
            },
        },
        before: function (obj) {
            layer.load();
        },
        done: function (result) {
            layer.closeAll('loading');
            console.log(result);
            if (result['status'] === 'SUCCESS') {
                layer.msg('upload ok!!!', {
                    time: 0,
                    end: function () {
                        url_param += '&sect_media=' + result['path'];
                    },
                    btn: ['confirm']
                })
            } else {
                layer.msg(result['error'], {
                    time: 0,
                    btn: ['confirm']
                })
            }

        },
        error: function () {
            layer.closeAll('loading');
            layer.msg(self.url);
        }
    });

    form.on('submit(submit_btn)', function () {
        tinyMCE.editors['sect_text'].save();

        if ($('#sect_name').val() === '') {
            layer.msg('课程名称为空', {time: 1000})
        } else if ($('#sect_tag').val() === '') {
            layer.msg('课程标签为空', {time: 1000})
        } else {
            $.ajax({
                url: '/teacher/submit_section/',
                type: 'POST',
                data: $('#sect_form').serialize() + url_param,
                cache: false,
                success: function (data) {
                    if (data['status'] === 'SUCCESS') {
                        layer.msg("OK!!!!", {
                            time: 0,
                            btn: ['confirm'],
                            end: function () {
                                location.href = '/teacher/course_info/' + sect_cour + '/';
                            }
                        });
                    } else if (data['error'] === 'None Type') {
                        layer.msg('章节关键信息为空', {
                            time: 0,
                            btn: ['confirm'],
                        })
                    } else {
                        layer.msg(data['status'], {
                            time: 0,
                            btn: ['confirm'],
                        })
                    }
                },
                error: function (xhr) {
                    layer.msg("FAIL...", {
                        time: 0,
                        btn: ['confirm'],
                    });
                    console.log(xhr);
                }
            });
        }

        return false;
    })
});
