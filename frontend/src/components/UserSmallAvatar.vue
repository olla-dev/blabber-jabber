<template>
    <div class='icon-container'>
        <!-- for the moment avatars are not handled in the backend-->
        <!-- so I'm just placing a random placeholder image -->
        <img src="https://picsum.photos/200/300" />
        <div v-if="user.profile!.online" class='status-circle logged-in' />
        <div v-if="!user.profile!.online" class='status-circle logged-out' />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'UserSmallAvatar',
    props: {
        user: {
            type: Object,
            required: true,
            default: () => ({ id: "", username: "", profile: {},  }),
        },
    },
});
</script>

<style lang="css">
.icon-container {
  width: 50px;
  height: 50px;
  position: relative;
}

img {
  height: 100%;
  width: 100%;
  border-radius: 50%;
}

.status-circle {
  width: 15px;
  height: 15px;
  border-radius: 50%;
  border: 2px solid white;
  bottom: 0;
  right: 0;
  position: absolute;
}
.logged-in {
  background-color: lightgreen;
}
.logged-out {
  background-color: lightgray;
}
</style>