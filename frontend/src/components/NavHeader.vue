<template>
    <nav class="navbar container" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
          <span class="icon">
            <i class="fa fa-message"></i>
          </span>&nbsp;
          <strong class="is-size-4">BlabberJabber</strong>
        </a>
        <a
          role="button"
          class="navbar-burger burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbarBasicExample"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>
      <div id="navbar" class="navbar-menu">
        <div class="navbar-start">
          <router-link v-if="isAuthenticated" to="/dashboard" class="navbar-item icon-text">
            <span class="icon">
                  <i class="fa fa-envelope"></i>
                </span>
                <span>Chat Rooms</span>
          </router-link>
          <router-link v-if="isAuthenticated" to="/profile" class="navbar-item icon-text">
              <span class="icon">
                <i class="fa fa-user"></i>
              </span>
              <span>Profile</span>
          </router-link>
        </div>
        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <router-link v-if="!isAuthenticated" to="/login" class="button is-info">
                <span class="icon">
                  <i class="fa fa-sign-in"></i>
                </span>
                <strong>Sign In</strong>
              </router-link>
              <router-link v-if="!isAuthenticated" to="/sign-up" class="button is-success">
                <span class="icon">
                  <i class="fa fa-user-plus"></i>
                </span>
                <strong>Sign Up</strong>
              </router-link>
              <button v-if="isAuthenticated" class="button is-dark" @click="doLogout()">
                <span class="icon">
                  <i class="fa fa-sign-out"></i>
                </span>
                <strong>Logout</strong>
              </button>
              <router-link to="/about" class="navbar-item icon-text button">
                  <span class="icon">
                    <i class="fa fa-info-circle"></i>
                  </span>
                  <span>About</span>
              </router-link>
            </div>
            </div>
        </div>
      </div>
    </nav>
  </template>
<script lang="ts">

    import userModule from '@/store/users';
    import { User } from '@/utils/types';
    export default {
      name: 'NavHeader',
      data() {
        return {
        }
      },
      computed: {
        // need annotation
        isAuthenticated(): boolean {
          return userModule.isAuthenticated
        },
        isLoading(): boolean {
          return userModule.isLoading
        },
        user(): User | undefined {
          return userModule.user
        }
      },
      methods: {
      },
    }
</script>
<style lang="scss">
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
    }


.navbar {
  height: 80px;
}
</style>