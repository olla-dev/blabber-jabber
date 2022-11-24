<template>
  <div class="container block">
    <form class="box org-description" @submit.prevent="submitForm">
      <h1 class="title">Sign Up</h1>
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <input class="input" type="text" v-model="username" placeholder="Username" required>
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <input class="input" type="text" v-model="email" placeholder="Email" required>
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
          </p>
        </div>
        <div class="field">
          <div class="columns">
            <div class="column">
                <p class="control has-icons-left has-icons-right">
                  <input class="input" type="text" v-model="firstname" placeholder="First name" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
            </div>
            <div class="column">
                <p class="control has-icons-left has-icons-right">
                  <input class="input" type="text" v-model="lastname" placeholder="Last name" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
            </div>
          </div>
        </div>
        <div class="field">
          <div class="columns">
            <div class="column">
                <p class="control has-icons-left">
                  <input class="input" type="password" v-model="password" placeholder="Password" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </p>
            </div>
            <div class="column">
                <p class="control has-icons-left">
                  <input class="input" type="password" v-model="verify_password" placeholder="Confirm Password" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-lock"></i>
                  </span>
                </p>
            </div>
          </div>
          
        </div>
        <div class="field">
          <p class="control icon-text is-large mt-5 mb-5">
            <span class="icon has-text-info">
              <i class="fas fa-info-circle"></i>
            </span>
            <span>By signing up you implicitly <strong>agree</strong> to the <router-link to="/terms">terms and conditions</router-link></span>
          </p>
        </div>
        <div class="field">
          <p class="control">
            <button type="submit" class="button is-success">
              Sign Up
            </button>
          </p>
        </div>
        </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'SignUpView',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    submitForm() {
      const formData = {
        username: this.username,
        password: this.password
      }
      axios.post('/api/v1/users/', formData).then(response => {
        console.log(response)
        this.$router.push('/login')
      }).catch(error => {
        console.error(error)
      })
    }
  }
}
</script>