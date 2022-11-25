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
        <div class="notification is-danger" v-if="loginError()">
          <button class="delete"></button>
          <ul>
            <li v-bind:key="index" v-for="(value, name, index) in error">
              <strong>{{name}}</strong>: <span v-for="(msg, idx) in value" v-bind:key="idx">{{msg}}</span>
            </li>
          </ul>
        </div>
        <div class="field">
          <p class="control icon-text is-large">
            <span class="icon has-text-info">
              <i class="fas fa-info-circle"></i>
            </span>
            <span>Forgot your password? <router-link to="/login">reset it</router-link></span>
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

<script lang="ts">
import { defineComponent } from 'vue';
import userModule from '@/store/users';

export default defineComponent({
  name: 'LoginView',
  data() {
    return {
      username: '',
      password: ''
    }
  },
  computed: {
    // need annotation
    isAuthenticated() {
      return userModule.isAuthenticated
    },
    errorCode() {
      return userModule.errorCode
    },
    error() {
      return userModule.error
    },
  },
  watch: {
    isAuthenticated: {
      handler(newVal, oldVal) {        
        if (oldVal != newVal && newVal == true) {
          this.goToDashboard();
        }
      },
      deep: true
    },
  },
  methods: {
    goToRegister () {
      this.$router.push('/register')
    },
    goToDashboard() {
      this.$router.push({ path: '/dashboard' });
    },
    goToForgotPassword () {
      alert('not implemented');
    },
    submitForm() {
      userModule.login({ username: this.username, password: this.password })
    },
    loginError() {
      return Object.keys(userModule.error).length != 0
    }
  },
})
</script>
