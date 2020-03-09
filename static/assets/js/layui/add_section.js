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
    url_param = '&sect_cour=' + sect_cour +
            '&sect_teacher=' + '1';

    upload.render({
        elem: '#upload_btn',
        url: '/teacher/upload/',
        accept: 'file',
        exts: 'mp4',
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
        done: function (result) {
            layer.msg('upload ok!!!', {
                time: 1000,
                end: function () {
                    url_param += '&sect_media=' + result['path'] + '&sect_tag=' + $('#sect_tag').val();
                }
            })
        },
        error: function () {
            layer.msg(self.url);
        }
    });

    form.on('submit(submit_btn)', function () {
        tinyMCE.editors['sect_text'].save();
        $.ajax({
            url: '/teacher/add_section/',
            type: 'POST',
            data: $('#sect_form').serialize() + url_param,
            cache: false,
            success: function (data) {
                if (data['status'] === 'SUCCESS') {
                    layer.msg("OK!!!!", {
                        time: 3000,
                        btn: ['confirm'],
                        end: function () {
                            // location.reload();
                        }
                    });
                } else {
                    layer.msg(data['status'], {
                        time: 5000,
                        btn: ['confirm']
                    })
                }
            },
            error: function (xhr) {
                layer.msg("FAIL...", {
                    time: 3000,
                    btn: ['confirm'],
                });
                console.log(xhr);
            }
        });
        return false;
    })
});
