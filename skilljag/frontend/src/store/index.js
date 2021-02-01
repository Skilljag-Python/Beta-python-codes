/* import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
 */

import Vuex from 'vuex'
import Vue from 'vue'
import axios from 'axios'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    user: {},
    skills: [],
    values: [],
    categories: [],
    states:[],
    cities:[],
    ads:[]
  },
  mutations: {

  },
  getters: {
    showCompleted: state => {
      return state.user.completed_at
    }
  },

  //to handle actions
  actions: {
    getInitData() {
      this.dispatch('getUser');
      this.dispatch('getSkills');
      this.dispatch('getValues');
      //this.dispatch('getCategories');
      this.dispatch('getStates');
      this.dispatch('getCities');
    },
    getSkills({
      commit
    }) {
      axios.get('/api/skills/')
        .then(r => {
          commit('SET_SKILLS', r.data)
        })
    },
    getValues({
      commit
    }) {
      axios.get('/api/values/')
        .then(r => {
          commit('SET_VALUES', r.data)
        })
    },
    getCategories({
      commit
    }) {
      axios.get('/api/categories/')
        .then(r => {
          commit('SET_CATEGORIES', r.data)
        })
    },
    getStates({
      commit
    }) {
      axios.get('/api/states/')
        .then(r => {
          commit('SET_STATES', r.data)
        })
    },
    getCities({
      commit
    }) {
      axios.get('/api/citys/')
        .then(r => {
          commit('SET_CITIES', r.data)
        })
    },
    getUser({
      commit
    }) {
      axios.get('/api/profiles/me/')
        .then(r => {
          commit('SET_USER', r.data)
          console.log(r.data.completed_at)
        })
    },
  },

  //to handle mutations
  mutations: {
    SET_SKILLS(state, v) {
      state.skills = v
    },
    SET_VALUES(state, v) {
      state.values = v
    },
    SET_CATEGORIES(state, v) {
      state.categories = v
    },
    SET_STATES(state, v) {
      state.states = v
    },
    SET_CITIES(state, v) {
      state.cities = v
    },
    SET_USER(state, v) {
      state.user = v
    },
  },
})

export default store
