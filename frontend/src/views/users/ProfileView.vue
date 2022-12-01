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
              <input class="input" type="text">
            </div>
          </div>
        </div>
        <div class="column">
          <div class="field">
            <label class="label">Last Name</label>
            <div class="control">
              <input class="input" type="text">
            </div>
          </div>
        </div>
      </div>
      

    <div class="field">
      <label class="label">Username</label>
      <div class="control has-icons-left has-icons-right">
        <input class="input" type="text" placeholder="username" disabled>
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
        <input class="input is-danger" type="email" placeholder="Email input">
        <span class="icon is-small is-left">
          <i class="fas fa-envelope"></i>
        </span>
        <span class="icon is-small is-right">
          <i class="fas fa-exclamation-triangle"></i>
        </span>
      </div>
      <p class="help is-danger">This email is invalid</p>
    </div>

    <div class="field">
      <label class="label">Bio</label>
      <div class="control">
        <input class="input" type="text">
      </div>
    </div>
    <div class="field">
      <label class="label">Facebook</label>
      <div class="control">
        <input class="input" type="text">
      </div>
    </div>
    <div class="field">
      <label class="label">Instagram</label>
      <div class="control">
        <input class="input" type="text">
      </div>
    </div>

    <div class="field is-grouped">
      <div class="control">
        <button class="button is-link">Update</button>
      </div>
    </div>
    </section>
  </div>
</template>

<script lang="ts">
export default {
  name: 'ProfileView',
}
</script>