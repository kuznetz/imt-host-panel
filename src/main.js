import Vue from 'vue'

import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'

import BootstrapVue from 'bootstrap-vue'

import CoreUi from '@coreui/vue'

import App from './App.vue'
import store from './store'
Vue.config.productionTip = false
Vue.component('fa-icon', FontAwesomeIcon)
library.add(fas)
Vue.use(BootstrapVue)
Vue.use(CoreUi)
document.body.classList.add('sidebar-show')
new Vue({
  store,
  render: h => h(App)
}).$mount('#app')
