<template>
        <div class="card chat-room">
            <nav class="navbar card-header" role="navigation" aria-label="main navigation">
                <div class="navbar-menu">
                    <div class="navbar-start">
                        <div class="navbar-item title">
                            <h2># <b>{{room.name}}</b></h2>
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
            <div class="card-content message-list" ref="messageContainer">
                <div class="columns">
                    <div class="column p-0" v-if="room">
                        <EmptyChatRoom v-if="room.messages.length == 0"/>
                        <MessageList 
                            v-else
                            :messages="room.messages" />
                        <UserTyping 
                            v-if="userTyping!.id"
                            :user="userTyping"
                            class="bottom-left"  />
                    </div>
                    <div class="column is-two-quarters top-right" v-if="userListShown">
                        <UserList :users="room.users" />
                    </div>
                </div>
            </div>
            <footer class="card-footer">
                <MessageEditText 
                    class="card-footer-item" 
                    @typing="isTyping"
                    @send="sendMessage"/>
            </footer>
        </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MessageEditText  from '@/components/MessageEditText.vue'
import UserList from '@/components/UserList.vue'
import MessageList from '@/components/MessageList.vue'
import EmptyChatRoom from '@/components/EmptyChatRoom.vue'
import UserTyping from '@/components/UserTyping.vue'
import { User } from '@/utils/types';
import chatRoomModule from '@/store/rooms';

export default defineComponent({
    name: 'ChatRoomView',
    components: {
        MessageEditText,
        UserList,
        MessageList,
        EmptyChatRoom,
        UserTyping
    },
    data() {
        return {
            userListShown: false,
            websocketConnection: {} as WebSocket
        }
    },
    computed: {
        userTyping(): User | undefined {
            return chatRoomModule.userTyping;
        },
    },
    mounted() {
        // init room websockt connection 
        this.initWebSocketConnection();
    },
    beforeUnmount() {
        this.websocketConnection.close();
    },
    props: {
        room: {
            type: Object,
            required: true,
            default: () => ({ id: "", name: "", users: -1, messages: [] }),
            // validator: (room) => ["id", "name", "users", "messages"].every((key) => key in room),
        },
        user: {
            type: Object,
            required: true,
            default: () => ({ id: "", username: "", profile: {},  }),
        },
    },
    methods: {
        requestLeaveChatRoom() {
            this.$emit('leave', { room: this.room.id})
        },
        showHideUserList() {
            this.userListShown = !this.userListShown;
        },
        isTyping() {
            // broadcast that current user is typing                        
            this.websocketConnection.send(
                JSON.stringify({
                    'command': 'typing',
                    'user': this.$props.user.id
                })
            );
        },
        sendMessage(event: any) {
            const message = event.message;
      
            this.websocketConnection.send(
                JSON.stringify({
                    'command': 'message',
                    'message': message,
                    'user': this.$props.user.id,
                    'room_id': this.$props.room.id
                })
            );
        },
        initWebSocketConnection() {
            console.log("Starting connection to Chat room channel")
            this.websocketConnection = new WebSocket(process.env.VUE_APP_WEBSOCKET_URL+'/room/'+this.room.name+'/');
            this.websocketConnection.onmessage = function (event: MessageEvent) {
                const eventJson = JSON.parse(event.data);
                
                switch (eventJson['type']) { 
                    case 'user_typing': {
                        const user_id = eventJson['user_id']                        
                        chatRoomModule.setUserTyping(user_id)                       
                        break;
                    }
                    case 'new_message': {
                        const message = eventJson['message'];                       
                        chatRoomModule.newMessage(message)                       
                        break;
                    }
                    default: 
                        break;
                }
            }
            this.websocketConnection.onopen = function (event: Event) {
                console.log("Successfully connected to the chat room channel...")
            }
        }
    },
    watch: { 
        room: function(newVal, oldVal) { 
            this.$el.scrollTop = this.$el.lastElementChild.offsetTop;
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
.bottom-left {
    margin: 5px;
    height: 30px;
    padding: 5px;
    min-width: 35%;
    text-overflow: clip;
    position: absolute;
    bottom: 80px;
    left: 0;
}
.top-right {
    margin: 5px;
    padding: 5px;
    min-width: 35%;
    text-overflow: clip;
    position: absolute;
    top: 80px;
    right: 15px;
}
</style>