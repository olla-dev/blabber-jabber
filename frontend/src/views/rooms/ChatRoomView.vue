<template>
    <div class="card">
        <header class="card-header">
            <div class="card-header-title">
                <h5 class="title">{{room.name}}</h5>
            </div>
            <button class="card-header-icon" aria-label="more options">
                <span class="icon">
                <i class="fas fa-user-group" aria-hidden="true"></i>
                </span>
            </button>
        </header>
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
    }
});
</script>