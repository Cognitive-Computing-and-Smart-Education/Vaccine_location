<template>
    <el-container style="height: 100%">
        <el-main>
            <container-center class="container-center"></container-center>
<!--            <el-amap class="amap-box" :vid="'amap-vue'" style="width:500px; height:300px"></el-amap>-->
        </el-main>
    </el-container>
</template>

<script>
    import ContainerLeft from './container/container-left'
    import ContainerCenter from './container/container-center'
    import ContainerRight from './container/container-right'
    import CurrentHead from '@/components/current-head'

    export default {
        name: "index",
        components: {
            ContainerLeft,
            ContainerCenter,
            ContainerRight,
            CurrentHead
        },
        data() {
            return {
                currentTime: ''
            };
        },
        created () {
            window.localStorage.clear()
            this.getNowTime()
        },
        methods: {
            timestampToTime(data) {
                let yyyy = data.getFullYear()
                let MM = (data.getMonth() + 1).toString().padStart(2, '0')
                let dd = data.getDate().toString().padStart(2, '0')
                let h = data.getHours().toString().padStart(2, '0')
                let m = data.getMinutes().toString().padStart(2, '0')
                let s = data.getSeconds().toString().padStart(2, '0')
                return yyyy + '年' + MM + '月' + dd + '日 ' + h + ':' + m + ':' + s
            },
            getNowTime() {
                let aData = new Date();

                this.currentTime = this.timestampToTime(aData)
            },
        }
    }
</script>

<style scoped>
    /deep/ .el-header, .el-footer {
        text-align: center;
        padding: 0;
    }

    /deep/ .el-main {
        background-color: #0e0f3c;
        color: #333;
        text-align: center;
        height: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0;
    }
    .container-center{
        width: 100%;
        height: 100%;
    }
</style>
