import config from './config.js'

class Api {
  token = null;

  async auth (username, password) {
    let result = await this.request('/auth/login', { username, password })
    if (result.token !== undefined) {
      this.token = result.token
    }
    return result
  }

  async logout () {
    let result = await this.request('/auth/logout', { token: this.token })
    this.token = null
    return result
  }

  async sitesList () {
    return this.request('/main/sites', { token: this.token })
  }

  async siteCreate (siteName) {
    return this.request('/main/create', { token: this.token, siteName })
  }

  async request (method, json) {
    console.log('request', method, json)
    const response = await fetch(config.host + method, {
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      method: 'POST',
      body: JSON.stringify(json)
    })
    const jsonResult = await response.json()
    console.log('jsonResult', jsonResult)
    return jsonResult
  }
}

export default (new Api())
