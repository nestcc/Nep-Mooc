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
    var sect_id = self.location.href.split('/')[5];
    url_param = '&sect_id=' + sect_id;


    upload.render({
        elem: '#reupload_btn',
        url: '/teacher/reupload/',
        accept: 'file',
        exts: 'mp4',
        size: 512000,
        data: {
            'csrfmiddlewaretoken': function () {
                return $('input:hidden').val()
            },
            'type': 'video',
            'sect_id': self.location.href.split('/')[5]
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
                    btn: ['confirm'],
                    end: function () {
                        location.reload()
                    }

                });
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
        $.ajax({
            url: '/teacher/update_section/',
            type: 'POST',
            data: $('#sect_form').serialize() + url_param,
            cache: false,
            success: function (data) {
                if (data['status'] === 'SUCCESS') {
                    layer.msg("OK!!!!", {
                        time: 0,
                        btn: ['confirm'],
                        end: function () {
                            // location.reload();
                        }
                    });
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
        return false;
    })
});

$('#del').click(function () {
    $.ajax({
            url: '/teacher/delete_section/',
            type: 'POST',
            data: {
            'csrfmiddlewaretoken': function () {
                return $('input:hidden').val()
            },
            'sect_id': self.location.href.split('/')[5]
        },
            cache: false,
            success: function (data) {
                // console.log(form.val("cour_form"));
                if (data['status'] === 'SUCCESS') {
                    layer.msg("OK!!!!", {
                        time: 0,
                        btn: ['confirm'],
                        end: function () {
                            location.href = data['url'];
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
