<template>
  <div class="row justify-content-center mt-4">
    <b-card title="Новый сайт" class="col-6">

      <b-input-group>
        <b-form-input v-model="siteName" placeholder="Имя сайта"></b-form-input>
        <b-input-group-append>
          <b-btn @click="create()" variant="primary">Создать</b-btn>
        </b-input-group-append>
      </b-input-group>

    </b-card>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '../api.js'

export default {
  name: 'NewSite',
  components: {
  },
  data () {
    return {
      'siteName': ''
    }
  },
  computed: mapState({
    sites: state => state.sites
  }),
  methods: {
    async create () {
      var result = await api.siteCreate(this.siteName)
      if (result.error !== undefined) {
        alert(result.error)
        return
      }
      await this.$store.dispatch('reloadSites')
      let curSite = this.sites.find((itm) => { itm.name == this.siteName })
      this.$store.commit('curSite', curSite)
    }
  }
}
</script>
