<template>
    <li>
        <a>
            <nav class="level p-0" @click="loadChatRoom">
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
                <div class="level-right" v-if="room.hasNewMessages">
                    <span class="tag is-danger">            
                        <i class="fa fa-message"></i>
                    </span>
                </div>
            </nav>
        </a>
    </li>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
    name: 'RoomListItem',
    props: {
        room: {
            type: Object,
            required: true,
            default: () => ({ id: "", name: "", users: -1, hasNewMessages: false }),
            // validator: (room) => ["id", "name", "users"].every((key) => key in room),
        },
    },
    methods: {
        loadChatRoom() {
            this.$emit('load', { room: this.room.id})
        }
    }
});
</script>