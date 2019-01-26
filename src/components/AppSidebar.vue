<template>
  <div class="sidebar" fixed>
    <!--SidebarHeader/-->
    <!--SidebarForm/-->

    <nav class="sidebar-nav">
        <ul class="nav">
          <li class="nav-item" v-for="(item, index) in items">
            <a @click.prevent="loadSite(item)" class="nav-link" :class="{ active: ((curItem !== null) && (curItem.name == item.name)) }" href="#"> <fa-icon icon="globe" /> {{item.name}}</a>
          </li>
          <li class="nav-item">
            <a @click.prevent="newSite()" class="nav-link" :class="{ active: (curItem === null) }" href="#"> <fa-icon icon="globe" /> Новый сайт</a>
          </li>
        </ul>
    </nav>

    <!-- <SidebarFooter/> -->
    <!-- SidebarMinimizer/ -->
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'AppSidebar',
  components: {},
  data () {
    return {}
  },
  computed: mapState({
    items: state => state.sites,
    curItem: state => state.curSite
  }),
  methods: {
    newSite () {
      this.$store.commit('curSite', null)
    },
    loadSite (item) {
      this.$store.commit('curSite', item)
    }
  }
}
</script>
