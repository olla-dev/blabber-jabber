<template>
    <div class="is-small">
        <input 
            class="input" 
            type="text" 
            v-model="message"
            @input="isTyping"
            placeholder="Write a new message"
            v-on:keyup.enter="sendMessage" />
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'MessageEditText',
    data() {
        return {
            message: ''
        }
    },
    methods: {
        sendMessage() {
            this.$emit('send', { message: this.message});
            this.message = '';
        },
        isTyping() {
            this.$emit('typing');
        }
    }
});
</script>