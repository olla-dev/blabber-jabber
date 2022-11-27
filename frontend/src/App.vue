<template>
  <div class="container">
    <section class="hero">
      <!-- Hero head: At the top -->
      <div class="hero-head m-0">
        <NavHeader />
        <notifications position="bottom right" />
      </div>
      <!-- Hero content: In the middle -->
      <div class="hero-body p-0 m-0">
        <router-view/>
      </div>
    </section>
  </div>
</template>

<script lang="ts">
  import NavHeader from './components/NavHeader.vue'
  export default {
    name: 'App',
    components: {
      NavHeader
    }
  }
</script>