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

});
