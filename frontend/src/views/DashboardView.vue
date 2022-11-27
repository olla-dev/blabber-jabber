<template>
    <div class="container"> 
      <div class="columns  dashboard is-gapless mb-5">
        <div class="column room-list card is-fifth mr-2">
              <aside class="menu pl-2 pr-2">
                <span class="menu-label mt-5">
                  Joined rooms  
                  <button class="button is-small ml-1" @click="refreshRooms">
                    <span class="icon is-small is-rounded">
                      <i class="fa fa-refresh"></i>
                    </span>
                  </button>
                  <button class="button is-small ml-1" @click="showJoinPanel">
                    <span class="icon is-small is-rounded">
                      <i class="fa fa-add"></i>
                    </span>
                  </button>
                </span>
                <Loading v-if="isLoading" />
                <ul v-else class="menu-list scrollable">
                  <RoomListItem v-for="room in rooms"
                        v-bind:key="room.id" @load="loadChatRoom" :room="room" />
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
            <ChatRoomView v-if="selectedChatRoom" :room="selectedChatRoom" />
            <JoinChatRoom @join="requestJoinChatRoom"  v-else/>
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
import JoinChatRoom from '@/views/rooms/JointChatRoom.vue';
import ChatRoomView from '@/views/rooms/ChatRoomView.vue';
import Loading from '@/components/Loading.vue';

export default defineComponent({
  name: "DashboardView",
  components: {
    RoomListItem,
    JoinChatRoom,
    ChatRoomView,
    Loading
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

    // init general websockt connection 
    this.initWebSocketConnection();
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
    loadChatRoom(event: any) {
      var room_id = event.room
      console.log('selected room:', room_id);
      chatRoomModule.setSelectedRoomById(room_id);
    },
    requestJoinChatRoom(event: any) {
      this.websocketConnection.send(
        JSON.stringify({
          'command': 'join',
          'room': event.room,
          'user': this.user.id
        })
      );
    },
    refreshRooms() {
      this.isLoading = true
      chatRoomModule.resetRooms();
      chatRoomModule.fetchRooms();
    },
    showJoinPanel() {
      chatRoomModule.setSelectedRoom(undefined);
    },
    initWebSocketConnection() {
      console.log("Starting connection to WebSocket Server")
      this.websocketConnection = new WebSocket(process.env.VUE_APP_WEBSOCKET_URL);
      this.websocketConnection.onmessage = function (event: MessageEvent) {
        const eventJson = JSON.parse(event.data);
        
        switch (eventJson['command']) {
          case 'join':
            var result = parseInt(eventJson['result']);
            
            if(result == 0) {
              chatRoomModule.fetchRooms();
              var room: ChatRoom = eventJson['room'];
              chatRoomModule.setSelectedRoom(room);
            }
            break;
          default:
            break;
        }
      }
      
      this.websocketConnection.onopen = function (event: Event) {
        console.log("Successfully connected to the chat websocket server...")
      }
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
      handler(newVal, oldVal) {
        if (oldVal != newVal) {
          this.isLoading = false;
        }
      },
      deep: true
    },
    selectedChatRoom: {
      handler(newVal, oldVal) {
        if (oldVal != newVal && newVal) {
          this.isLoading = false;
        }
      },
      deep: true
    }
  },
})
</script>


<style>
.dashboard {
  width: 100%;
  height: calc(100vh - 80px);
}
.room-list {
  overflow: scroll;
}
.scrollable {
  overflow-y: scroll; 
  width: 100%;
}
</style>