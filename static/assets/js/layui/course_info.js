layui.use(['table', 'carousel'], function () {
    var table = layui.table;
    var carousel = layui.carousel;

    table.init( 'stu_list', {
        page: {layout: ['count', 'prev', 'page', 'next', 'skip']},
        limit: 5,
    });

    table.init( 'sect_list', {
        page: {layout: ['count', 'prev', 'page', 'next', 'skip']},
        limit: 5,
    });

    table.on('row(stu_list)', function (obj) {
        var data = obj.data;
        //
        layer.open({
            type: 2,
            shade: false,
            area: ['1000px', '700px'],
            maxmin: true,
            content: '/teacher/learn_detail/' + obj.data['id'] + '/',
        })

    });


    table.on('row(sect_list)', function (obj) {
        window.location.href='/teacher/edit_section_info/' + obj.data['id'] + '/';
    });

    carousel.render({
        elem: '#status_chart',
        width: '100%',
        height: '400px',
        arrow: 'none'
    })
});