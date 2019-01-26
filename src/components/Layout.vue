<template>
  <div class="app">
    <Header fixed>
      <b-navbar-brand href="/">ImtHosting</b-navbar-brand>
      <!--b-navbar-nav class="d-md-down-none">
        <b-nav-item class="px-3" to="/dashboard">Dashboard</b-nav-item>
        <b-nav-item class="px-3" to="/users" exact>Users</b-nav-item>
        <b-nav-item class="px-3">Settings</b-nav-item>
      </b-navbar-nav-->
      <b-navbar-nav class="ml-auto" style="margin-right: 10px;">
        <b-nav-item @click="logout" class="d-md-down-none">
          <fa-icon icon="sign-out-alt" />
          Выход
        </b-nav-item>
      </b-navbar-nav>
    </Header>
    <div class="app-body">
      <AppSidebar fixed />
      <main class="main">
        <div class="container">
          <Site v-if="curSite !== null"></Site>
          <NewSite v-else></NewSite>
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import AppSidebar from './AppSidebar.vue'
import Site from './Site.vue'
import NewSite from './NewSite.vue'
import api from '../api.js'

export default {
  name: 'Layout',
  components: {
    AppSidebar,
    Site,
    NewSite
  },
  data () {
    return {}
  },
  computed: mapState({
    curSite: state => state.curSite
  }),
  methods: {
    logout () {
      api.logout()
      this.$store.commit('authorized', null)
    }
  },
  async mounted () {
    this.$store.dispatch('reloadSites')
  }
}
</script>
