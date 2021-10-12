export default {
    state: {
        className: '高一（1）班',
        schoolYear: '',
        grade: ''
    },
    getters: {
        className(state) {
            return state;
        }
    },
    mutations: {
        changeClassName(state, payload) {
            state = payload;
        }
    },
    actions: {

    }
}
