<template>
    <div class="card">
        <header class="card-header">
            <p class="card-header-title">
                room_name
            </p>
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
});
</script>