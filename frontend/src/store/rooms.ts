import {
  Module,
  VuexModule,
  MutationAction,
  Mutation,
  getModule
} from 'vuex-module-decorators'
import { ChatRoom } from '@/utils/types/index'
import { chatRoomApi } from '@/api/api.service'
import store from './index'

@Module({ dynamic: true, store, name: 'chat-rooms' })
class ChatRoomModule extends VuexModule {
  rooms: ChatRoom[] = [];
  selectedChatRoom: ChatRoom | undefined = undefined;

  /**
   * Returns a specific Vessel by its vessel_id
   */
  get chatRoom() {
    return (room_id: number) => {
      this.rooms.find(
        room => room.id === room_id
      )
    };
  }

  get getSelectedRoom(): ChatRoom | undefined {
    return this.selectedChatRoom;
  }

  @Mutation
  setSelectedRoom(room_id: number) {
    this.selectedChatRoom = this.rooms.find(room => room.id === room_id);
  }

  @MutationAction
  async fetchRooms() {
    const rooms = await chatRoomApi.fetchRooms();
    return { rooms }
  }
}

const chatRoomModule = getModule(ChatRoomModule)
export default chatRoomModule