<template>
    <div class="notification">
    <article class="media p-2">
        <figure class="media-left">
            <UserSmallAvatar class="media-left" :user="user" />
        </figure>
        <div class="media-content">
            <div class="content">
            <p>
                <b>{{user.first_name}} {{user.last_name}}</b> <small>{{formatDate(message.sent_time_utc)}}</small>
                <br>
                {{message.content}}
            </p>
            </div>
        </div>
    </article>
</div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import moment from 'moment';
import UserSmallAvatar from './UserSmallAvatar.vue';

export default defineComponent({
    name: 'MessageItem',
    components: {
        UserSmallAvatar
    },
    props: {
        message: {
            type: Object,
            required: true,
            default: () => ({ id: -1, author_id: -1, content: "", sent_time_utc: "" }),
        },
        user: {
            type: Object,
            required: true,
            default: () => ({ id: "", username: "", profile: {},  }),
        }
    },
    methods: {
        formatDate(date: Date) {
            return moment(date).utc().format('YYYY/MM/DD HH:mm');
        }
    }
});
</script>