<template>
    <div class="card">
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
                            <button class="card-header-icon" aria-label="more options">
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
        <div class="card-content">
            <section class="section is-large">
            aaa
            </section>
        </div>
        <footer class="card-footer">
            <MessageEditText class="card-footer-item" />
        </footer>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MessageEditText  from '@/components/MessageEditText.vue'

export default defineComponent({
    name: 'ChatRoomView',
    components: {
        MessageEditText
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
        }
    }
});
</script>