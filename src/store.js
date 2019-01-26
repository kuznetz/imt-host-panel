import Vue from 'vue'
import Vuex from 'vuex'
import api from './api.js'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: null,
    sites: [],
    curSite: null
  },
  mutations: {
    authorized (state, token) {
      state.token = token
    },
    sites (state, newSites) {
      state.sites = newSites
    },
    curSite (state, site) {
      state.curSite = site
    }
  },
  actions: {
    async reloadSites ({ commit }) {
      let newSites = await api.sitesList()
      commit('sites', newSites)
    }
  }
})
