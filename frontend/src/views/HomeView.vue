<template>
  <div class="content">
    qqq
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import chatRoomModule from '@/store/rooms';
import { ChatRoom } from '@/utils/types';

export default defineComponent({
  name: "HomeView",
  data() {
    return {
      isLoading: false,
      websocketConnection: new WebSocket(process.env.VUE_APP_WEBSOCKET_URL)
    }
  },
  mounted() {
    this.isLoading = true
    chatRoomModule.fetchRooms();
  },
  created: function () {
    console.log("Starting connection to WebSocket Server")
    this.websocketConnection.onmessage = function (event: MessageEvent) {
      const eventJson = JSON.parse(event.data);
    }

    this.websocketConnection.onopen = function (event: Event) {
      console.log(event)
      console.log("Successfully connected to the chat websocket server...")
    }
  },
  computed: {
    // need annotation
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

      const id = `${this.selectedChatRoom?.id}`;
    }
  },
  watch: {
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