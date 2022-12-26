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
                  <input class="input" type="text" v-model="first_name" placeholder="First name" required>
                  <span class="icon is-small is-left">
                    <i class="fas fa-user"></i>
                  </span>
                </p>
            </div>
            <div class="column">
                <p class="control has-icons-left has-icons-right">
                  <input class="input" type="text" v-model="last_name" placeholder="Last name" required>
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
                  <input class="input" type="password" v-model="re_password" placeholder="Confirm Password" required>
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
            <span>By signing up you implicitly <strong>agree</strong> to the <router-link to="/sign-up">terms and conditions</router-link></span>
          </p>
        </div>

        <div class="notification is-danger" v-if="formError">
          <button class="delete"></button>
          {{formError}}
        </div>
        <div class="notification is-danger" v-if="registrationError()">
          <button class="delete"></button>
          <ul>
            <li v-bind:key="index" v-for="(value, name, index) in error">
              <strong>{{name}}</strong>: {{msgArray(value)}}
            </li>
          </ul>
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

<script lang="ts">
import { defineComponent } from 'vue';
import userModule from '@/store/users';

export default defineComponent({
  name: 'SignUpView',
  data() {
    return {
      username: '',
      password: '',
      re_password: '',
      first_name: '',
      last_name: '',
      email: '',
      formError: ''
    }
  },
  beforeMount() {
    // reset the flag that tracks registration status
    userModule.setRegistrationSuccess(false);
  },
  computed: {
    // need annotation
    registrationSuccess() {
      return userModule.registrationSuccess
    },
    errorCode() {
      return userModule.errorCode
    },
    error() {
      return userModule.error
    },
  },
  watch: {
    registrationSuccess: {
      handler(newVal, oldVal) {        
        if (oldVal != newVal && newVal == true) {
          this.goToLogin();
        }
      },
      deep: true
    },
  },
  methods: {
    goToLogin() {
      this.$router.push({ path: '/login' });
    },
    submitForm() {
      if (this.password !== this.re_password) {
        this.formError = 'Password confirmation failed.'
      } else {
        userModule.register({
          username: this.username,
          password: this.password,
          re_password: this.re_password,
          email: this.email,
          first_name: this.first_name,
          last_name: this.last_name
        });
      }
    },
    registrationError() {
      return Object.keys(userModule.error).length != 0
    },
    msgArray(msg: Array<string>) {
      return msg.join(', ')
    }
  }
})
</script>