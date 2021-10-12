import Vue from 'vue'
import Vuex from 'vuex'
import home from './modules/home'
import routerData from './modules/routerData'
import classData from './modules/classData'
import collapseType from './modules/collapseType'



Vue.use(Vuex)

export default new Vuex.Store({
    // strict: true,
    state: {
        styleName: '' //风格名称。
    },
    getters: {

    },
    mutations: {

    },
    modules: {
        home,
        routerData,
        classData,
        collapseType
    },
    actions: {

    }
})
