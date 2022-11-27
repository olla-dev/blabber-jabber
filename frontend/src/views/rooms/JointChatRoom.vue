<template>
    <div class="card">
        <div class="card-content is-centered">
            <section class="section is-large">
                <div class="field">
                    <h1 class="title">Chat room</h1>
                    <h2 class="subtitle">Join the conversation</h2>
                </div>
                <div class="field">
                    <p class="control has-icons-left has-icons-right">
                        <input class="input" v-model="room_name" type="text" placeholder="Type chat room name">
                        <span class="icon is-small is-left">
                            <i class="fas fa-hashtag"></i>
                        </span>
                    </p>
                </div>
                <div class="field">
                    <p class="control">
                        <button :disabled="!room_name" class="button is-success" @click="joinChatRoom()">
                        Join
                        </button>
                    </p>
                </div>
            </section>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'JoinChatRoom',
    data() {
        return {
            room_name: '',
            websocketConnection: {} as WebSocket
        }
    },
    methods: {
        joinChatRoom() {
            this.$emit('join', { room: this.room_name});
        }
    }
});
</script>