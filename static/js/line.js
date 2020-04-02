var line = echarts.init(document.getElementById('left'));
option_line = {
    title: {
        text: ''
    },
    tooltip: {
        trigger: 'axis'
    },
    legend: {
        data: []
    },
    grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    toolbox: {
        feature: {
            saveAsImage: {}
        }
    },
    xAxis: {
        type: 'category',
        boundaryGap: false,
        data: []
    },
    yAxis: {
        type: 'value'
    },
    series: [
        {
            name: '',
            type: 'line',
            stack: '总量',
            data: []
        },
        {
            name: '',
            type: 'line',
            stack: '总量',
            data: []
        },

    ]
};


line.setOption(option_line);