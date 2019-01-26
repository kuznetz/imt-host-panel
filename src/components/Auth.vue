<template>
<div class="app flex-row align-items-center">
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8 col-lg-6">
        <div class="card-group">
          <div class="card p-4">
            <form class="card-body" @submit.prevent="login()">
              <h1>Test server</h1>
              <p class="text-muted">Imt host panel</p>
              <div class="input-group mb-3">
                <div class="input-group-prepend"><span class="input-group-text"><fa-icon icon="user" /></span></div>
                <input v-model="username" class="form-control" type="text" placeholder="Пользователь">
              </div>
              <div class="input-group mb-4">
                <div class="input-group-prepend"><span class="input-group-text"><fa-icon icon="key" /></span></div>
                <input v-model="password" class="form-control" type="password" placeholder="Пароль">
              </div>
              <div class="row">
                <div class="col-12 text-center">
                  <div v-if="error != ''" class="alert alert-danger" role="alert">
                    {{error}}
                  </div>
                  <button class="btn btn-primary px-4" type="submit">
                    <fa-icon v-if="loading" icon="slash" spin /> Войти
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import api from '../api.js'

export default {
  name: 'Auth',
  data () {
    return {
      username: '',
      password: '',
      error: '',
      loading: false
    }
  },
  methods: {
    async login () {
      this.error = ''
      this.loading = true
      const jsonResult = await api.auth(this.username, this.password)
      this.loading = false
      if (jsonResult.error !== undefined) {
        this.error = jsonResult.error
        return
      }
      this.$store.commit('authorized', jsonResult.token)
    }
  }
}
</script>
