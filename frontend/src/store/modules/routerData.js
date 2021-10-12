export default {
    state: {
        path: '',
        oldRouter: {}
    },
    getters: {
        routerPath(state) {
            return state.path;
        }
    },
    mutations: {
        changeRouterPath(state, payload) {
            state.path = payload;
        },
        changeOldRouterPath(state,payload) {
            state.oldRouter = payload;
        }
    },
    actions: {

    }
}
