<template>
  <div class="container">
    <div class="hero is-primary mb-10">
      <div class="hero-body">
        <div class="container">
          <h1 class="title is-size-1">Profile</h1>
        </div>
      </div>
    </div>
    <section class="box mb-15">
      <div class="columns">
        <div class="column">
          <div class="field">
            <label class="label">First Name</label>
            <div class="control">
              <input class="input" type="text" 
                v-model="user!.first_name">
            </div>
          </div>
        </div>
        <div class="column">
          <div class="field">
            <label class="label">Last Name</label>
            <div class="control">
              <input class="input" type="text" 
                v-model="user!.last_name">
            </div>
          </div>
        </div>
      </div>
      

    <div class="field">
      <label class="label">Username</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" 
          type="text" 
          placeholder="username" 
          v-model="user!.username"
          disabled>
        <span class="icon is-small is-left">
          <i class="fas fa-user"></i>
        </span>
        <span class="icon is-small is-right">
          <i class="fas fa-check"></i>
        </span>
      </div>
    </div>

    <div class="field">
      <label class="label">Email</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" 
          v-model="user!.email"
          type="email" 
          disabled
          placeholder="Email input">
        <span class="icon is-small is-left">
          <i class="fas fa-envelope"></i>
        </span>
      </div>
    </div>

    <div class="field">
      <label class="label">Bio</label>
      <div class="control">
        <input class="input" 
          type="text" 
          v-model="user!.profile!.bio">
      </div>
    </div>
    <div class="field">
      <label class="label">Facebook</label>
      <div class="control">
        <input class="input" 
          v-model="user!.profile!.social_facebook"
          type="text">
      </div>
    </div>
    <div class="field">
      <label class="label">Instagram</label>
      <div class="control">
        <input class="input" 
          v-model="user!.profile!.social_instagram"
          type="text">
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link" @click="updateProfile">Update</button>
      </div>
    </div>
    </section>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import userModule from '@/store/users';
export default defineComponent({
  name: 'ProfileView',
  computed: {
    user() {
      return userModule.user;
    },
  },
  methods: {
    updateProfile() {
      userModule.updateProfile(this.user);
    }
  }
})
</script>