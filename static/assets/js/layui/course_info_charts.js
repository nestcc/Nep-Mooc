var stu_chart = echarts.init(document.getElementById('stu_chart'), 'light');
var cour_chart = echarts.init(document.getElementById('cour_chart'), 'light');
var cour_id = location.href.split('/')[5];

stu_chart.setOption({
    title: {
        text: '学习进度前十'
    },
    tooltip: {},
    legend: {
        data:['完成章节数量']
    },
    xAxis: {data: []},
    yAxis: {},
    series: [{
        name: '完成章节数量',
        type: 'bar',
        data: []
    }]
});

cour_chart.setOption({
    title: {
        text: '7天内学习章节数量'
    },
    tooltip: {},
    legend: {
        data:['章节数量']
    },
    xAxis: {data: []},
    yAxis: {},
    series: [{
        name: '章节数量',
        type: 'bar',
        data: []
    }]
});

stu_chart.showLoading();
cour_chart.showLoading();

$.get('/teacher/get_stu_top10_chart/' + cour_id + '/').done(function (data) {
    stu_chart.hideLoading();
    console.log(data['x_data']);
    stu_chart.setOption({
        xAxis: {data: data['x_data']},
        series: [{
            name: '完成章节数量',
            data: data['y_data']
        }]
    })
});

$.get('/teacher/get_last_week_chart/' + cour_id + '/').done(function (data) {
    cour_chart.hideLoading();
    console.log(data['x_data']);
    cour_chart.setOption({
        xAxis: {data: data['x_data']},
        series: [{
            name: '章节数量',
            data: data['y_data']
        }]
    })
});