<template>
    <div class="container-right-box">
        <div class="public-sentiment-box">
            <div class="current-title finger" @click="goDetail('/detailsHome/schoolProfile', 'schoolProfile')">
                办学规模
            </div>
            <div class="current-content" style="display: flex">
                <div style="width: 70%;height: 100%">
                    <div class="surveyBox1">
                        <div class="surveyBox2">
                            <div class="surveyBox3">
                                <div class="surveyTitle">教学班数量</div>
                                <div class="surveyVal">
                                    {{ scale.teachingClassNum }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                        <div class="surveyBox2">
                            <div class="surveyBox3">
                                <div class="surveyTitle">课程总量</div>
                                <div class="surveyVal">
                                    {{ scale.totalCourses }}
                                    <span>门</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <img src="../../../assets/img/home-img.png" class="scaleImg">
                </div>
                <div style="width: 30%;height: 100%">
                    <div class="surveyBox1" style="margin-bottom: 10px">
                        <div class="surveyBox2" style="width: 100%">
                            <div class="surveyBox3">
                                <div class="surveyTitle">教学班数量</div>
                                <div class="surveyVal">
                                    {{ scale.teachingClassNum }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="surveyBox1" style="margin-bottom: 10px">
                        <div class="surveyBox2" style="width: 100%">
                            <div class="surveyBox3">
                                <div class="surveyTitle">教学班数量</div>
                                <div class="surveyVal">
                                    {{ scale.teachingClassNum }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="surveyBox1" style="margin-bottom: 10px">
                        <div class="surveyBox2" style="width: 100%">
                            <div class="surveyBox3">
                                <div class="surveyTitle">教学班数量</div>
                                <div class="surveyVal">
                                    {{ scale.teachingClassNum }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="surveyBox1">
                        <div class="surveyBox2" style="width: 100%">
                            <div class="surveyBox3">
                                <div class="surveyTitle">教学班数量</div>
                                <div class="surveyVal">
                                    {{ scale.teachingClassNum }}
                                    <span>个</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="information-sources-box">
            <div class="current-title finger" @click="goDetail('/detailsHome/teacherAnalysis/teacherProfile', 'teacherProfile')">
                师资概况
            </div>
            <div class="current-content">
                <div class="teacherMessage">
                    <span>双师高质教师占比</span>
                    {{ teacherForm.highQuality }}
                </div>
                <div class="teacherMessage">
                    <span>具有研究生教师占专任教师占比</span>
                    {{ teacherForm.graduateStudent }}
                </div>
                <div class="teacherMessage">
                    <span>具有高级职务教师占专任教师占比</span>
                    {{ teacherForm.seniorPosition }}
                </div>
                <div id="teacherProfileChart"></div>
            </div>
        </div>
        <div class="media-impression">
            <div class="current-title finger" @click="goDetail('/detailsHome/studentsSource', 'studentsSource')">
                本期招生数据
            </div>
            <div class="current-content">
                <div id="enrollmentDataChart"></div>
            </div>
        </div>
    </div>
</template>

<script>
    import {  } from '@/api/Home'
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "container-left",
        data() {
            return {
                teacherForm: {
                    highQuality: '49%',
                    graduateStudent: '23%',
                    seniorPosition: '13%'
                },
                scale: {
                    teachingClassNum: '123',
                    totalCourses: '1234'
                }
            };
        },
        computed: {
            ...mapGetters(["homeAreaName"]),
        },
        watch: {
            homeAreaName() {
                this.init(this.homeAreaName);
            }
        },
        mounted() {
            this.init()
        },
        methods: {
            init(Area_name) {
                this.getEnrollmentDataChart(Area_name || '')
                this.getTeacherProfileChart(Area_name || '')
            },
            goDetail(path,name) {
                window.localStorage.setItem('activeAside', name)
                this.$router.push({
                    path: path,
                })
            },
            getTeacherProfileChart() {
                let myChart = this.$echarts.init(document.getElementById('teacherProfileChart'))
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        orient: 'vertical',
                        top: 'center',
                        right: 30,
                        itemWidth: 18,
                        itemHeight: 10,
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        },
                        pageIconSize: 12
                    },
                    series: [
                        {
                            name: '访问来源',
                            type: 'pie',
                            top: 10,
                            right: 120,
                            radius: '100%',
                            avoidLabelOverlap: false,
                            labelLine: {
                                show: false
                            },
                            label: {
                                show: false,
                                position: 'center'
                            },
                            data: [
                                {value: 64, name: '校内专任教师',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '校内普通教师',itemStyle: {color: '#60a8ff'}},
                                {value: 12, name: '校外兼职教师',itemStyle: {color: '#e8d83b'}},
                                {value: 23, name: '校外聘请教师',itemStyle: {color: '#e6823f'}},
                            ]
                        }
                    ]
                })
            },
            getEnrollmentDataChart() {
                let myChart = this.$echarts.init(document.getElementById('enrollmentDataChart'))
                // 绘制图表
                myChart.setOption({
                    tooltip: {
                        trigger: 'item',
                        transitionDuration: 0,
                    },
                    legend: {
                        type: 'scroll',
                        top: '0',
                        left: 'center',
                        itemWidth: 18,
                        itemHeight: 10,
                        textStyle: {
                            color: '#fff',
                            fontSize: 12
                        },
                        pageIconSize: 12
                    },
                    series: [
                        {
                            name: '访问来源',
                            type: 'pie',
                            top: 20,
                            radius: ['50%', '70%'],
                            avoidLabelOverlap: false,
                            data: [
                                {value: 1048, name: '统招招生',itemStyle: {color: '#13acb5'}},
                                {value: 123, name: '自主招生',itemStyle: {color: '#60a8ff'}},
                            ]
                        }
                    ]
                })
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
    #enrollmentDataChart{
        width: 100%;
        height: 100%;
    }
    #teacherProfileChart{
        width: 100%;
        height: calc(100% - 72px);
    }
    .teacherMessage{
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: #fff;
        font-size: 12px;
        margin-bottom: 5px;
    }
    .teacherMessage span{
        color: #146BCA;
    }
    .surveyBox1{
        padding: 0px 10px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .surveyBox2{
        /*padding: 10px;*/
        width: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .surveyBox3{
        text-align: left;
    }
    .surveyTitle{
        font-size: 12px;
        color: #fff;
    }
    .surveyVal{
        font-size: 20px;
        font-weight: bolder;
        color: #e6823f;
    }
    .surveyVal span{
        font-size: 12px;
        color: #e6823f;
    }
    .scaleImg{
        width: 80%;
        height: calc(100% - 81px);
        margin: 20px auto 0;
        display: inline-block;
    }
</style>
