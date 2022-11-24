<template>
  <div class="container block">
    <form class="box org-description" @submit.prevent="submitForm">
      <h1 class="title">Login</h1>
        <div class="field">
          <p class="control has-icons-left has-icons-right">
            <input class="input" type="text" v-model="username" placeholder="Username" required>
            <span class="icon is-small is-left">
              <i class="fas fa-envelope"></i>
            </span>
            <span class="icon is-small is-right">
              <i class="fas fa-check"></i>
            </span>
          </p>
        </div>
        <div class="field">
          <p class="control has-icons-left">
            <input class="input" type="password" v-model="password" placeholder="Password" required>
            <span class="icon is-small is-left">
              <i class="fas fa-lock"></i>
            </span>
          </p>
        </div>
        <div class="field">
          <p class="control icon-text is-large">
            <span class="icon has-text-info">
              <i class="fas fa-info-circle"></i>
            </span>
            <span>Forgot your password? <router-link to="/reset-password">reset it</router-link></span>
          </p>
        </div>
        <div class="field">
          <p class="control">
            <button type="submit" class="button is-success">
              Login
            </button>
          </p>
        </div>
        </form>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    loading: {
      get () {
        return this.$store.state.users.loading
      },
      set () {
        this.$store.commit('users/setLoading')
      }
    },
    loggedIn: {
      get () {
        return this.$store.state.users.loggedIn
      }
    },
    fetchError: {
      get () {
        return this.$store.state.users.fetchError
      }
    },
    fetchErrorCode: {
      get () {
        return this.$store.state.users.fetchErrorCode
      }
    }
  },
  methods: {
    goToRegister () {
      this.$router.push('/register')
    },
    goToForgotPassword () {
      this.$router.push('/forgot-password')
    },
    submitForm() {
      this.$store.dispatch('users/login', {
            username: this.username,
            password: this.password
      })
    }
  }
}
</script>
