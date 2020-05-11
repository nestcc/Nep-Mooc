var course_chart = echarts.init(document.getElementById('course_chart'), 'light');

course_chart.setOption({
    title: {
        text: '课程类型情况'
    },
    tooltip: {},
    legend: {
        data:['数量']
    },
    xAxis: {data: []},
    yAxis: {},
    series: [{
        name: '数量',
        type: 'bar',
        data: []
    }]
});

course_chart.showLoading();

$.get('/teacher/get_index_chart/').done(function (data) {
    course_chart.hideLoading();
    console.log(data['x_data']);
    course_chart.setOption({
        xAxis: {data: data['x_data']},
        series: [{
            name: '数量',
            data: data['y_data']
        }]
    })
});


