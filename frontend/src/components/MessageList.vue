<template>
    <aside class="menu pl-2 pr-2 box">
        <ul class="menu-list scrollable">
            <MessageItem v-for="(message, index) in messages"
                v-bind:key="index" :message="message!" :user="getMessageAuthor(message!)" />
        </ul>
    </aside>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import chatRoomModule from '@/store/rooms';
import { Message } from '@/utils/types';

import MessageItem from './MessageItem.vue';

export default defineComponent({
    name: "MessageList",
    components: { MessageItem },
    props: {
        messages: {
            type: Array,
            required: true,
            default: () => ([{ 
                id: -1,  
                chat_room_id: -1,
                author_id: -1, 
                content: "", 
                sent_time_utc: ""
            }]),
        },
    },
    methods: {
        getMessageAuthor(message: any) {
            const chatRoom = chatRoomModule.chatRoom(message.chat_room_id);
            return chatRoomModule.user(chatRoom!, message.author_id);
        }
    }
});
</script>