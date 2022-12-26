<template>
    <div class="is-medium ml-2 notification">
        <span class="icon has-text-info">
            <i class="fas fa-info-circle"></i>
        </span> No messages yet..
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'EmptyChatRoom'
});
</script>