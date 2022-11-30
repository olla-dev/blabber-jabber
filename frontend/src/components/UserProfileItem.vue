<template>
    <article class="media p-2">
        <figure class="media-left">
            <UserSmallAvatar class="media-left" :user="user" />
        </figure>
        <div class="media-content">
            <div class="content">
            <p>
                <strong>{{user.first_name}} {{user.last_name}}</strong> <small>@{{user.username}}</small>
                <br>
                <small>{{user.profile!.bio}}</small>
            </p>
            </div>
        </div>
    </article>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import UserSmallAvatar from './UserSmallAvatar.vue';

export default defineComponent({
    name: 'UserProfileItem',
    components: {
        UserSmallAvatar
    },
    props: {
        user: {
            type: Object,
            required: true,
            default: () => ({ id: "", username: "", profile: {},  }),
        },
    },
});
</script>