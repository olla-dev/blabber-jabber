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
          <router-link to="/" class="navbar-item icon-text">
              <span class="icon">
                <i class="fa fa-envelope"></i>
              </span>
              <span>Chat Rooms</span>
          </router-link>
          
        </div>
        <div class="navbar-end">
        <div class="navbar-item">
          <router-link to="/about" class="navbar-item icon-text button">
                <span class="icon">
                  <i class="fa fa-info-circle"></i>
                </span>
                <span>About</span>
            </router-link>
        </div>
      </div>
      </div>
    </nav>
  </template>
<script lang="ts">
    export default {
      name: 'NavHeader',
      computed: {
        
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