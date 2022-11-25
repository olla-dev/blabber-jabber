<template>
  <div class="container">
    <div class="is-centered">
      
    <section class="hero is-dark">
      <div class="hero-body">
        <div class="container">
          <h1 class="title" data-cy="home-welcome-message">Welcome to BlabberJabber</h1>
          <h2 class="subtitle">
            Realtime Chat
          </h2>
          <div class="button-block">
            <button class="button is-xl is-dark">
              <span class="icon">
                <i class="fa fa-user-plus"></i>
              </span>
              <span>Sign Up or Login to chat</span>
            </button>
          </div>
        </div>
      </div>
    </section>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import userModule from '@/store/users';

export default defineComponent({
  name: "HomeView",
  data() {
    return {
      isLoading: false,
    }
  },
  mounted() {
    this.isLoading = true
    console.log(this.isAuthenticated);
    
    if(this.isAuthenticated == true) {
      this.goToDashboard();
    }
  },
  computed: {
    // need annotation
    isAuthenticated() {
      return userModule.isAuthenticated
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
    goToDashboard() {
      this.$router.push({ path: '/dashboard' });
    },
  },
})
</script>


<style>
#dashboard {
  width: 100%;
  height: calc(100vh - 80px);
}
</style>