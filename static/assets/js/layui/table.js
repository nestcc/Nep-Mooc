layui.use('table', function () {
    var table = layui.table;

    table.init('course', {
        limit: 20
    });

    table.on('row(course)', function (obj) {
        var data = obj.data;
        //
        // layer.alert(JSON.stringify(data), {
        //     title: '当前行数据：'
        // });

        self.location.href = "/teacher/course_info/" + data["id"];

        // //标注选中样式
        // obj.tr.addClass('layui-table-click').siblings().removeClass('layui-table-click');
    });
});