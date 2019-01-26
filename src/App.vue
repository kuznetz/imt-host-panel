<template>
  <Auth v-if="token === null"></Auth>
  <Layout v-else></Layout>
</template>

<script>
import Auth from './components/Auth.vue'
import Layout from './components/Layout.vue'
import { mapState } from 'vuex'

export default {
  name: 'app',
  computed: mapState({
    token: state => state.token
  }),
  components: {
    Auth, Layout
  }
}
</script>

<style lang="scss">
  @import "@coreui/coreui/scss/coreui.scss";
</style>
