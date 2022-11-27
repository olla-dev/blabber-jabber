<template>
  <div class="container">
    <div class="columns is-centered">
      <div class="column">
        <div class="box">
          <a v-for="room in rooms" v-bind:key="room.id" class="panel-block is-active">
          <span class="panel-icon">
            <i class="fas fa-book" aria-hidden="true"></i>
          </span>
          {{room.name}}
        </a>
        </div>
      </div>
      <div class="column is-four-fifths">
        <div class="box">
          <section class="section is-large">
            <div class="hero-body">
                <div class="container">
                    messages in the selected room
                </div>
            </div>

            <footer class="hero-foot">
                message footer
            </footer>
          </section>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import chatRoomModule from '@/store/rooms';
import userModule from '@/store/users';
import { ChatRoom } from '@/utils/types';

export default defineComponent({
  name: "DashboardView",
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