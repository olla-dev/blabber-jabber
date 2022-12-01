<template>
    <div class="container">
      <div class="columns  dashboard is-gapless mb-5">
        <div class="column room-list card is-fifth mr-2">
          <aside class="menu pl-2 pr-2">
            <span class="menu-label mt-5">
              Joined rooms ({{rooms.length}})
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
            <Loading v-if="isLoading && rooms.length > 0" />
            <ul v-else class="menu-list scrollable">
              <RoomListItem v-for="room in rooms" :notification="room.hasNewMessages"
                    v-bind:key="room.id" @load="loadChatRoom" :room="room" />
            </ul>
          </aside>
        </div>
        <div class="column is-four-fifths">
            <router-view :key="$route.fullPath"/>
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
import Loading from '@/components/Loading.vue';

export default defineComponent({
  name: "DashboardView",
  components: {
    RoomListItem,
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
    this.$router.push({ path: '/dashboard/join'})
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
      this.$router.push({ name: "ChatRoomView", params: {id: room_id}})
    },
    requestJoinChatRoom(event: any) {
      var room = this.rooms.find(room => room.name == event.room);
      if (room) {
        this.$notify({
          type: "success",
          text: "You are already member of this chat room!",
        });
        chatRoomModule.setSelectedRoom(room);
      } else {
        this.websocketConnection.send(
          JSON.stringify({
            'command': 'join',
            'room': event.room,
            'user': this.user.id
          })
        );
      }
    },
    requestLeaveChatRoom(event: any) {
      console.log('Leave room:', event.room);
      
      this.websocketConnection.send(
        JSON.stringify({
          'command': 'leave',
          'room': event.room,
          'user': this.user.id
        })
      );
    },
    refreshRooms() {
      this.isLoading = true;
      chatRoomModule.fetchRooms();
    },
    showJoinPanel() {
      chatRoomModule.setSelectedRoom(undefined);
    },
    initWebSocketConnection() {
      console.log("Starting connection to WebSocket Server")
      let notify = this.$notify;
      this.websocketConnection = new WebSocket(process.env.VUE_APP_WEBSOCKET_URL+'/lobby/');
      this.websocketConnection.onmessage = function (event: MessageEvent) {
        const eventJson = JSON.parse(event.data);
        const room: ChatRoom = eventJson['room'];
        const room_id = parseInt(eventJson['room_id']);
        const result = parseInt(eventJson['result']); 

        switch (eventJson['command']) {
          case 'user_status_update':            
            chatRoomModule.setUserStatus({
              user_id: eventJson['user'], 
              status: JSON.parse(eventJson['online'])
            });
            break;
          case 'chat_room_update': {
            if(!room_id) {
              chatRoomModule.fetchRooms();
            } else {
              chatRoomModule.roomNotification(eventJson);
            }
            break;
          }
          case 'join':            
            if(result == 0) {
              chatRoomModule.fetchRooms();
              chatRoomModule.setSelectedRoom(room);

              notify({
                type: "success",
                text: "Welcome to "+room.name,
              });
            } else {
              notify({
                type: "danger",
                text: "An error has occured: "+eventJson["reason"],
              });
            }
            break;
          case 'leave':            
            if(result == 0) {
              notify({
                type: "success",
                text: "You left "+room.name,
              });
              chatRoomModule.fetchRooms();
              chatRoomModule.setSelectedRoom(undefined);
            } else {
              notify({
                type: "danger",
                text: "An error has occured: "+eventJson["reason"],
              });
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
        if (newVal.length > 0) {
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
}
.room-list {
  overflow: scroll;
}
.scrollable {
  overflow-y: scroll; 
  width: 100%;
}
</style>