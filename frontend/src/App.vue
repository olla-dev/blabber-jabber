<template>
    <div class="container pb-20 pt-1">
      <!-- Hero head: At the top -->
      <div class="hero-head m-0">
        <NavHeader />
        <notifications position="bottom right" />
      </div>
      <!-- Hero content: In the middle -->
      <div class="hero-body p-0 m-0">
        <router-view/>
      </div>
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