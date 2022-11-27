<template>
    <div class="container"> 
      <div class="columns is-gapless mb-5">
        <div class="column card is-fifth mr-2">
              <aside class="menu pl-2 pr-2">
                <p class="menu-label mt-3">
                  Joined rooms  
                </p>
                <ul class="menu-list">
                  <li>
                    <a>
                      <RoomListItem 
                        v-for="room in rooms"
                        v-bind:key="room.id" 
                        :room="room" />
                    </a>
                  </li>
                </ul>
                <p class="menu-label mt-3">
                  Other rooms  
                </p>
                <ul class="menu-list">
                  <li>
                    <a>
                      todo
                    </a>
                  </li>
                </ul>
              </aside>
        </div>
        <div class="column is-four-fifths">
            <ChatRoomView v-if="selectedChatRoom" />
            <JoinChatRoom v-else/>
        </div>
      </div>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import chatRoomModule from '@/store/rooms';
import userModule from '@/store/users';
import { ChatRoom } from '@/utils/types/types';
import RoomListItem from '@/components/RoomListItem.vue';
import JoinChatRoom from '@/components/JointChatRoom.vue';
import ChatRoomView from '@/views/rooms/ChatRoomView.vue';

export default defineComponent({
  name: "DashboardView",
  components: {
    RoomListItem,
    JoinChatRoom,
    ChatRoomView
  },
  data() {
    return {
      isLoading: false,
      websocketConnection: {} as WebSocket
    }
  },
  mounted() {
    this.isLoading = true
    // fetch user profile
    userModule.profile();
    // fetch chat rooms from REST API
    chatRoomModule.fetchRooms();

    console.log("Starting connection to WebSocket Server")
    this.websocketConnection = new WebSocket(process.env.VUE_APP_WEBSOCKET_URL);
    this.websocketConnection.onmessage = function (event: MessageEvent) {
      // const eventJson = JSON.parse(event.data);
    }

    this.websocketConnection.onopen = function (event: Event) {
      console.log("Successfully connected to the chat websocket server...")
    }
  },
  beforeUnmount() {
    this.websocketConnection.close();
  },
  computed: {
    user() {
      return userModule.user;
    },
    rooms(): ChatRoom[] {
      return chatRoomModule.rooms
    },
    selectedChatRoom(): ChatRoom | undefined {
      return chatRoomModule.getSelectedRoom
    }
  },
  methods: {
    loadChatRoom() {
      console.log('selected room:', this.selectedChatRoom?.id);
    }
  },
  watch: {
    user: {
      handler(newVal, oldVal) {
        if (newVal.profile) {
          if(newVal!.profile!.is_banned) {
            alert('Your account is banned');
            userModule.logout();
            this.$router.push({ path: '/'})
          }
        }
      },
      deep: true
    },
    rooms: {
      handler(oldVal, newVal) {
        if (oldVal != newVal) {
          this.isLoading = false;
        }
      },
      deep: true
    },
    selectedChatRoom: {
      handler(oldVal, newVal) {
        if (oldVal != newVal) {
          this.isLoading = false;
          this.loadChatRoom();
        }
      },
      deep: true
    }
  },
})
</script>


<style>
#dashboard {
  width: 100%;
  height: calc(100vh - 80px);
}
</style>