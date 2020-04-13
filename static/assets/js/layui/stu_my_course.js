var onclick_id = 0;
var csrf_token = $('input:hidden').val();

layui.use(['laypage', 'layer'], function () {
    var laypage = layui.laypage;
    var layer = layui.layer;

    laypage.render({
        elem: 'lay-page',
        count: $('#item_number').html(),
        curr: location.href.split('/')[5],
        limit: 4,
        jump: function(obj, first){
            console.log(obj.curr);
            if (!first){
                location.href = '/student/my_course/' + obj.curr + '/';
            }
        }
    })
});

function view_page(id) {
    location.href = '/student/course_page/' + id + '/';
}