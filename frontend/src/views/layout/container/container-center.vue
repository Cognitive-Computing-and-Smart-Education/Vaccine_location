<template>
    <div>
        <div class="map-box">
            <center-map></center-map>
        </div>
    </div>
</template>

<script>
    import '../../../../node_modules/echarts/map/js/china.js'
    import centerMap from './center-map'
    import { getNewsNum, getNewsMap, getAreaNewsIndustry } from '@/api/Home'
    import { mapGetters, mapMutations } from "vuex";

    export default {
        name: "container-center",
        data() {
            return {
                courseOverview: {
                    total: '705',
                    courseType: '58',
                    onLineCourse: '106',
                    openClass: '231'
                },
                studentProfile: {
                    enrollmentRate: '98',
                    threeGoodStudents: '21',
                    keyUniversities: '65',
                    poorNum: '41'
                }
            };
        },
        components: {
            centerMap
        },
        computed: {
            ...mapGetters(["homeAreaName"]),
        },
        watch: {
            homeAreaName() {

            }
        },
        mounted () {
            this.init();
        },
        methods: {
            ...mapMutations(["changeHomeAreaName"]),
            // async
            init() {

            },
            goDetail(path,name) {
                window.localStorage.setItem('activeAside', name)
                this.$router.push({
                    path: path,
                })
            }
        }
    }
</script>

<style scoped>
    .map-box{
        width: 100%;
        height: 100%;
    }
    .surveyVal span{
        font-size: 12px;
        color: #fff;
    }
</style>
