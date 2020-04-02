
function get_c_data() {

    $.ajax({
        url: "/data",
        success: function (data) {
            option_bar.title.text = '学历分布情况'
            option_bar.xAxis.data = data['sort']
            option_bar.series[0].data = data['lis']
            bar.setOption(option_bar)
        },
        error: function () {
           alert("发送ajax请求失败")
        }

    })

}

function get_l_data(){
    $.ajax({
        url: "/l_data",
        success: function (data) {
            // alert(data['name'])
            option_line.title.text = '年龄分布情况'
            option_line.legend.data = ['女性', '男性']
            option_line.series[0].name = '女性'
            option_line.series[1].name = '男性'
            option_line.xAxis.data = data['name']
            option_line.series[0].data = data['lis_wom']
            option_line.series[1].data = data['lis_man']
            line.setOption(option_line)

        }

    })
}

function get_r_data(){
    $.ajax({
        url: "/r_data",
        success: function (data) {

            option_pies.legend.data = data['name']
            option_pies.series[0].data = data['data']
            option_pies.series[0].name = '月收入'
            option_pies.title.text = '月收入占比'
            pies.setOption(option_pies)

        }

    })
}

get_c_data()
get_l_data()
get_r_data()
// setInterval(get_data,10000*10)