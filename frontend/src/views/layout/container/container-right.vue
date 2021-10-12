<template>
    <div class="container-right-box">
        <div class="public-sentiment-box">
            <div class="current-title finger" @click="goDetail('/detailsHome/graduationAnalysis', 'graduationAnalysis')">
                升学情况
            </div>
            <div class="current-content">
                <div id="enrollmentChart"></div>
            </div>
        </div>
        <div class="information-sources-box">
            <div class="current-title finger" @click="goDetail('/detailsHome/studentAnalysis/studentQuality', 'studentQuality')">
                学生获奖（学年）
            </div>
            <div class="current-content">
                <div id="awardChart"></div>
            </div>
        </div>
        <div class="media-impression">
            <div class="current-title finger" @click="goDetail('/detailsHome/socialEvaluation', 'socialEvaluation')">
                学校社会影响分析
            </div>
            <div class="current-content">
                <div id="influenceChart"></div>
            </div>
        </div>
    </div>
</template>

<script>
    import {  } from '@/api/Home'
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "container-right",
        data() {
            return {

            };
        },
        computed: {
            ...mapGetters(["homeAreaName"]),
        },
        watch: {
            homeAreaName() {
                this.init(this.homeAreaName)
            }
        },
        components: {

        },
        mounted () {
            this.init();
        },
        methods: {
            init(Area_name) {
                this.getEnrollmentChart(Area_name || '')
                this.getAwardChart(Area_name || '')
                this.getInfluenceChart(Area_name || '')
            },
            goDetail(path,name) {
                window.localStorage.setItem('activeAside', name)
                this.$router.push({
                    path: path,
                })
            },
            getInfluenceChart() {
                let myChart = this.$echarts.init(document.getElementById('influenceChart'))
                myChart.setOption({
                    tooltip: {
                        trigger: 'axis',
                        transitionDuration: 0
                    },
                    grid: {
                        right: 10,
                        left: 10,
                        top: 10,
                        bottom: 10,
                        containLabel: true
                    },
                    radar: {
                        // shape: 'circle',
                        center: ['50%', '65%'],
                        radius: '85%',
                        indicator: [
                            {
                                name: '名声影响力',
                                max: 100
                            },{
                                name: '看法影响力',
                                max: 100
                            },{
                                name: '意见影响力',
                                max: 100
                            }
                        ],
                        axisLine: { // (圆内的几条直线)坐标轴轴线相关设置
                            lineStyle: {
                                opacity: 0.3
                            }
                        },
                        splitLine: {
                            lineStyle: {
                                opacity: 0.3
                            }
                        }
                    },
                    series: [{
                        name: '社会影响力',
                        type: 'radar',
                        tooltip: {
                            trigger: 'item'
                        },
                        symbolSize: 2,
                        data: [
                            {
                                value: [67, 85, 21],
                                name: '社会影响力',
                                areaStyle: {
                                    opacity: 0.2
                                }
                            },
                        ]
                    }]
                })
            },
            getAwardChart() {
                let myChart = this.$echarts.init(document.getElementById('awardChart'))
                myChart.setOption({
                    grid: {
                        right: 20,
                        left: 10,
                        top: 30,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['技能比赛获奖', '学科竞赛获奖', '文体比赛获奖', '其他比赛获奖'],
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        // boundaryGap: false,
                        data: ['2017', '2018', '2019', '2020', '2021'],
                        axisLabel: {
                            color: '#fff'
                        }
                    },
                    yAxis: {
                        type: 'value',
                        splitLine: {
                            lineStyle: {
                                color: '#142852'
                            }
                        },
                        axisLabel: {
                            color: '#fff'
                        }
                    },
                    series: [
                        {
                            name: '技能比赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [320, 302, 301, 334, 390]
                        },
                        {
                            name: '学科竞赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [120, 132, 101, 134, 90]
                        },
                        {
                            name: '文体比赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [220, 182, 191, 234, 290]
                        },
                        {
                            name: '其他比赛获奖',
                            type: 'bar',
                            stack: 'total',
                            emphasis: {
                                focus: 'series'
                            },
                            barWidth: 25,
                            data: [150, 212, 201, 154, 190]
                        }
                    ]
                })
            },
            getEnrollmentChart(Area_name){
                let myChart = this.$echarts.init(document.getElementById('enrollmentChart'))
                // 绘制图表
                myChart.setOption({
                    tooltip: {},
                    grid: {
                        right: 20,
                        left: 10,
                        top: 30,
                        bottom: 10,
                        containLabel: true
                    },
                    legend: {
                        data: ['一本人数', '二本人数', '专科人数'],
                        textStyle: {
                            color: '#fff'
                        }
                    },
                    xAxis: {
                        type: 'category',
                        boundaryGap: false,
                        data: ['2017', '2018', '2019', '2020', '2021'],
                        axisLabel: {
                            color: '#fff'
                        }
                    },
                    yAxis: {
                        type: 'value',
                        splitLine: {
                            lineStyle: {
                                color: '#142852'
                            }
                        },
                        axisLabel: {
                            color: '#fff'
                        }
                    },
                    series: [{
                            name: '一本人数',
                            type: 'line',
                            stack: '总量',
                            smooth: true,
                            data: [101, 134, 90, 230, 210]
                        },
                        {
                            name: '二本人数',
                            type: 'line',
                            stack: '总量',
                            smooth: true,
                            data: [91, 234, 290, 330, 310]
                        },
                        {
                            name: '专科人数',
                            type: 'line',
                            stack: '总量',
                            smooth: true,
                            data: [201, 154, 190, 330, 410]
                        }]
                });

            }
        }
    }
</script>

<style scoped>
    .container-right-box>div{
        height: calc((100% - 30px) / 3);
        border: 1px solid #1e2252;
        margin-bottom: 15px;
        box-sizing: border-box;
    }
    .container-right-box>div:last-child{
        margin-bottom: 0;
    }
    .current-title:before{
        content: '';
        display: inline-block;
        width: 4px;
        height: 18px;
        background-color: #e6c23c;
        margin-right: 8px;
    }
    .current-title{
        height: 42px;
        display: flex;
        color: #fff;
        align-items: center;
        justify-content: flex-start;
        width: 100%;
        /*margin-bottom: 10px;*/
        padding: 8px 15px;
        background-image: linear-gradient(to right, rgba(20,107,202,1) , rgba(20,107,202,0));
        /*#146bca*/
    }
    .current-content{
        width: 100%;
        height: calc(100% - 42px);
        border: 1px solid #1e2252;
        border-top: none;
        padding: 10px;
    }
    #enrollmentChart,
    #awardChart,
    #influenceChart{
        width: 100%;
        height: 100%;
    }
</style>
