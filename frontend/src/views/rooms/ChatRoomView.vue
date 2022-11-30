<template>
        <div class="card chat-room">
            <nav class="navbar card-header" role="navigation" aria-label="main navigation">
                <div class="navbar-menu">
                    <div class="navbar-start">
                        <div class="navbar-item">
                            # <b>{{room.name}}</b>
                        </div>
                    </div>
                    <div class="navbar-end">
                        <div class="navbar-item">
                            <div class="buttons">
                                <button @click="showHideUserList" class="card-header-icon" aria-label="more options">
                                    <span class="icon">
                                    <i class="fas fa-user-group" aria-hidden="true"></i>
                                    </span>
                                </button>
                                <button @click="requestLeaveChatRoom" class="card-header-icon" aria-label="more options">
                                    <span class="icon">
                                    <i class="fa fa-sign-out" aria-hidden="true"></i>
                                    </span>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>
            <div class="card-content message-list">
                <div class="columns">
                    <div class="column">
                        Auto
                    </div>
                    <div class="column is-two-quarters" v-if="userListShown">
                        <UserList :users="room.users" :is-loading="false" />
                    </div>
                </div>
            </div>
            <footer class="card-footer">
                <MessageEditText class="card-footer-item" />
            </footer>
        </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MessageEditText  from '@/components/MessageEditText.vue'
import UserList from '@/components/UserList.vue'

export default defineComponent({
    name: 'ChatRoomView',
    components: {
        MessageEditText,
        UserList
    },
    data() {
        return {
            userListShown: false,
        }
    },
    props: {
        room: {
            type: Object,
            required: true,
            default: () => ({ id: "", name: "", users: -1 }),
            // validator: (room) => ["id", "name", "users"].every((key) => key in room),
        },
    },
    methods: {
        requestLeaveChatRoom() {
            this.$emit('leave', { room: this.room.id})
        },
        showHideUserList() {
            this.userListShown = !this.userListShown;
        }
    }
});
</script>

<style lang="scss">
.chat-room {
  height: calc(100vh - 80px);
}
.message-list {
  overflow: scroll;
  height: 80%;
}
</style>