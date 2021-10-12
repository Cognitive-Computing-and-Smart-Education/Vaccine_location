export default {
    state: {
        collapseType: '全国'
    },
    getters: {
        collapseTypeName(state) {
            return state.collapseType;
        }
    },
    mutations: {
        changeCollapseTypeName(state, payload) {
            state.collapseType = payload;
        }
    },
    actions: {

    }
}
