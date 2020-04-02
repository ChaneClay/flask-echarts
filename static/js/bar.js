// 基于准备好的dom，初始化echarts实例
var bar = echarts.init(document.getElementById('main'));

// 指定图表的配置项和数据
var option_bar = {
    title: {
        text: ''
    },
    tooltip: {},
    legend: {
        data:['学历']
    },
    xAxis: {
        data: []
    },
    yAxis: {},
    series: [{
        name: '学历',
        type: 'bar',
        data: []

    }]
};

// 使用刚指定的配置项和数据显示图表。

bar.setOption(option_bar);