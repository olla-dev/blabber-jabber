<template>
    <nav class="level p-0">
        <!-- Left side -->
        <div class="level-left is-5">
            <div class="level-item">
                <a class="panel-block">
                    <span class="panel-icon">
                        <i class="fas fa-hashtag" aria-hidden="true"></i>
                    </span>
                    {{room.name}}

                </a>
            </div>
        </div>

        <!-- Right side -->
        <div class="level-right">
            <span class="tag is-rounded is-danger">11</span>
                
        </div>
    </nav>



    
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'RoomListItem',
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