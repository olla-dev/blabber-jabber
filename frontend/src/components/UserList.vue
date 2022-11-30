<template>
    <aside class="menu pl-2 pr-2 box">
        <span class="menu-label mt-5 mb-1">
            Members ({{users.length}})
        </span>
        <ul class="menu-list scrollable">
            <UserProfileItem v-for="(user, index) in users"
                v-bind:key="index" :user="user!" />
        </ul>
    </aside>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import UserProfileItem from './UserProfileItem.vue';

export default defineComponent({
    name: "UserList",
    components: { UserProfileItem },
    props: {
        users: {
            type: Array,
            required: true,
            default: () => ([{ id: "", username: "", profile: {},  }]),
        },
    },
    methods: {
        refreshUsers() {
            this.$emit('load-users');
        }
    }
});
</script>