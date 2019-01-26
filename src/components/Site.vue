<template>
  <div class="mt-2">
    <div class="float-right">
      <b-button size="large" variant="success">Починить права</b-button>
      <b-button size="large" variant="primary" class="ml-1">Выключить</b-button>
      <b-button size="large" variant="danger" class="ml-1">Удалить</b-button>
    </div>
    <h2>{{site.name}}</h2>
    <b-tabs>
      <b-tab title="Nginx" active>
        <div class="row">
          <div class="col-8">
            <h4>Основные</h4>
            <div class="row">
              <div class="col-7 mb-1">
                <input class="form-control" placeholder="Основной домен">
              </div>
              <div class="col-1 mb-1 text-center h3">
                :
              </div>
              <div class="col-4 mb-1">
                <input class="form-control" placeholder="Порт">
              </div>
              <div class="col-6 mb-1">
                <select class="form-control"><option>Без шаблона</option></select>
              </div>
              <div class="col-6 mb-1">
                <select class="form-control"><option>Без https</option></select>
              </div>
            </div>

            <div class="form-group">
              <label for="nginxSource">Исходный код nginx:</label>
              <textarea class="form-control" id="nginxSource" rows="18"></textarea>
            </div>

          </div>
          <div class="col-4">
            <div class="form-group">
              <h4>Доп домены</h4>
              <textarea class="form-control" rows="6"></textarea>
              <small>С этих доменов будет перенаправление на основной</small>
            </div>
            <div class="form-group">
              <h4>PHP</h4>
              <select class="form-control mb-1"><option>Не использовать</option></select>
              <div class="row">
                <div class="col-4 mb-1">
                  <label class="">Процессы:</label>
                </div>
                <div class="col-4 mb-1">
                  <input class="form-control" placeholder="Мин">
                </div>
                <div class="col-4 mb-1">
                  <input class="form-control" placeholder="Макс">
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="text-center">
          <b-button size="large" variant="success" class="ml-1">Сохранить</b-button>
        </div>
      </b-tab>
      <b-tab title="GIT" >
        <br>2. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
        officia deserunt mollit anim id est laborum.
      </b-tab>
      <b-tab title="Логи" >
        <br>3. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
        officia deserunt mollit anim id est laborum.
      </b-tab>
      <b-tab title="SSH Доступ" >
        <br>3. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore
        et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
        aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
        dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
        officia deserunt mollit anim id est laborum.
      </b-tab>
    </b-tabs>
  </div>
</template>

<script>
import { mapState } from 'vuex'
import api from '../api.js'

export default {
  name: 'Site',
  components: {
  },
  data () {
    return {}
  },
  computed: mapState({
    site: state => state.curSite
  }),
  methods: {
  },
  async mounted () {
  }
}
</script>
